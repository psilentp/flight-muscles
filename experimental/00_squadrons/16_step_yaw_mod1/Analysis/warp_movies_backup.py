import flylib
import db_access as dba
from pylab import *
fly_db = dba.get_db()

GMR22H05_list = [308,309,310,311,312,313,314,315,316,317,327,328] #range(317,326)
GMR22H05_swarm = flylib.Squadron(fly_db,GMR22H05_list)
GMR39E01_list = [318,319,320,321,322,323,324,325,329,330,331,332,333,334,335,336]
GMR39E01_swarm = flylib.Squadron(fly_db,GMR39E01_list)



class Basis(dict):    
    def __setitem__(self,key,item):
        """overload the __setitem__ method of dict so the transform and inverse
         transform matrices are computed when the basis vectors are changed"""
        try:
            if key in ['a1','a2']:
                dict.__setitem__(self,key,item)
                A = np.vstack((self['a1'],self['a2'])).T
                A_inv = np.linalg.inv(A)
                self['A'] = A
                self['A_inv'] = A_inv
            else:
                dict.__setitem__(self,key,item)
        except KeyError:
            dict.__setitem__(self,key,item)
                
        
class GeometricModel(object):   
    def __init__(self,lines,basis):
        self.lines = lines
        self.basis = basis
        ## put lines in barycentric coords
        self.barycentric = dict()
        for key in self.lines.keys():
            coords = dot(self.basis['A_inv'],(self.lines[key]-self.basis['p'][:,newaxis])) 
            self.barycentric[key] = coords.T
            
    def coords_from_basis(self,basis):
        ret = dict()
        for key in self.barycentric.keys():
            coords = np.dot(basis['A'],(self.barycentric[key]).T)+basis['p'][:,newaxis]
            ret[key] = coords
        return(ret)

class ModelView(object):
    def __init__(self,model):
        self.model = model
        
    def plot(self,basis,**kwargs):
        lines = self.model.coords_from_basis(basis)
        plot_args = {}
        plot_args['plot_frame'] = kwargs.pop('plot_frame',True)
        plot_args['frame_head_width'] = kwargs.pop('frame_head_width',20)
        plot_args['contour_color'] = kwargs.pop('contour_color','w')
        
        kwargs['color'] = plot_args['contour_color']
        for line in lines.values():
            plot(line[0,:],line[1,:], **kwargs)
        if plot_args['plot_frame']:
            p = basis['p']
            a1 = basis['a1']
            a2 = basis['a2']
            kwargs['color'] = 'g'
            kwargs['head_width'] = plot_args['frame_head_width']
            arrow(p[0],p[1],a1[0],a1[1],**kwargs)
            kwargs['color'] = 'b'
            kwargs['head_width'] = plot_args['frame_head_width']
            arrow(p[0],p[1],a2[0],a2[1],**kwargs)
            
    def get_masks(self,basis):
        from matplotlib.path import Path
        lines = self.model.coords_from_basis(basis)
        paths = {}
        [paths.update({k:Path(lines[k].T)}) for k in lines]
        x,y = meshgrid(range(130),range(174))
        pnts = vstack((x.ravel(),y.ravel())).T
        masks = {}
        [masks.update({k:paths[k].contains_points(pnts)}) for k in paths]
        [masks.update({k:masks[k]}) for k in masks]
        return masks


###add position of large setae 
import cPickle as cpkl
f = open('model_data.cpkl','rb')
model_data = cpkl.load(f)
f.close()
model_data['e1'] = array([[ 170.02788104,  326.71685254],
                             [ 380.98203222,  919.92627014]])
model_data['e2'] = array([[ 172.83333333,  332.83333333],
                          [ 551.5       ,  164.83333333]])
e1 = model_data['e1']
e2 = model_data['e2']
muscles = dict()

for key in model_data.keys():
    if not(key in ['e1','e2']):
        muscles[key] = model_data[key]
        
confocal_basis = Basis()
confocal_basis['a1'] = e2[1]-e2[0]
confocal_basis['a2'] = e1[1]-e2[0]
confocal_basis['p'] = e2[0]
musc = GeometricModel(muscles,confocal_basis)
mv = ModelView(musc)


testfly = GMR22H05_swarm.flies[0]
flydir = testfly.fly_path
imgs = testfly.experiments.values()[0].exp_record['tiff_data']['images']
num_frames = shape(imgs)[0]
output_shape = (num_frames,1024/4,1024/4)
import h5py
warped_movie_file = h5py.File(flydir + 'warped_movie_compressed.hdf5')
dset = warped_movie_file.create_dataset('images',(output_shape),compression = "gzip")

def X(tup):
	import cv2
	img,Ap = tup
	X_warped = cv2.warpAffine(img.T,Ap,(1024/4,1024/4))
	return(X_warped)


def warp_fly_movie(fly,input_dset,output_dset,chunksize = 40):
    import cv2
    from multiprocessing import Pool
    import cPickle
    pkname = fly.fly_path + '/basis_fits.cpkl'
    f = open(pkname);img_data = cPickle.load(f);f.close()
    test_basis = Basis()
    #print data.keys()
    for key in ['A','p','a1','a2']:
        test_basis[key] = img_data[key]
    src_p0 = test_basis['a1'] + test_basis['p']
    src_p1 = test_basis['p']
    src_p2 = test_basis['a2'] + test_basis['p']
    dst_p0 = confocal_basis['a1'] + confocal_basis['p']
    dst_p1 = confocal_basis['p']
    dst_p2 = confocal_basis['a2'] + confocal_basis['p']
    A = cv2.getAffineTransform(np.float32([src_p0,src_p1,src_p2]),np.float32([dst_p0,dst_p1,dst_p2]))
    #compose to smaller image size
    A = vstack((A,[0,0,1]))
    S = np.array([[0.25,0,0],[0,0.25,0],[0,0,1]])
    Ap = dot(S,A)[:2,:3]
    for i in range(shape(input_dset)[0])[::chunksize]:
    	if (i+chunksize > shape(input_dset)[0]):
    		end_idx = shape(input_dset)[0]
    	else:
    		end_idx = i+chunksize
    	idxs = range(i,end_idx)
    	print idxs
        frames = [(np.array(imgs[x]),Ap) for x in idxs]
        pool = Pool() 
        warped = pool.map(X, frames) 
        for warped_idx,out_idx in enumerate(idxs):
        	output_dset[out_idx] = warped[warped_idx]

warp_fly_movie(testfly,imgs,dset,chunksize = 100)
imshow(dset[5],cmap = cm.gray)
savefig('outtest')






