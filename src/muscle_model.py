##Library for aligning muscle models to the thorax of the fly
import numpy as np

class Frame(dict):    
    def __setitem__(self,key,item):
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

    def load(self,filepath):
        """load from a pickled dictionary"""
        import cPickle
        pkname = filepath
        f = open(pkname);data = cPickle.load(f);f.close()
        for key in data.keys():
            self[key] = data[key]

    def get_transform(self,other):
        """get transform into self from other frame"""
        A1 = np.hstack((self['A'],self['p'][:,np.newaxis]))
        A2 = np.hstack((other['A'],other['p'][:,np.newaxis]))
        A1 = np.vstack((A1,[0,0,1]))
        A2 = np.vstack((A2,[0,0,1]))
        return(np.dot(A1,np.linalg.inv(A2)))

class GeometricModel(object):   
    def __init__(self,lines = None,frame = None,filepath = None):
        if not(filepath is None):
            self.load(filepath)
        else:
            self.construct(lines,frame)

    def construct(self,lines,frame):
        self.lines = lines
        self.frame = frame
        ## put lines in barycentric coords
        self.barycentric = dict()
        for key in self.lines.keys():
            coords = np.dot(self.frame['A_inv'],(self.lines[key]-self.frame['p'][:,np.newaxis])) 
            self.barycentric[key] = coords.T
            
    def load(self,filepath):
        """load from a pickled dictionary"""
        import cPickle as cpkl
        fi = open(filepath)
        model_data = cpkl.load(fi)
        fi.close()
        model_data['e1'] = np.array([[ 170.02788104,  326.71685254],
                             [ 380.98203222,  919.92627014]])
        model_data['e2'] = np.array([[ 172.83333333,  332.83333333],
                          [ 551.5       ,  164.83333333]])
        e1 = model_data['e1']
        e2 = model_data['e2']
        muscles = dict()
        for key in model_data.keys():
            if not(key in ['e1','e2']):
                muscles[key] = model_data[key]
        confocal_frame = Frame()
        confocal_frame['a1'] = e2[1]-e2[0]
        confocal_frame['a2'] = e1[1]-e2[0]
        confocal_frame['p'] = e2[0]
        self.construct(muscles,confocal_frame)

    def coords_from_frame(self,other_frame):
        ret = dict()
        for key in self.barycentric.keys():
            coords = np.dot(other_frame['A'],(self.barycentric[key]).T) + \
                     other_frame['p'][:,np.newaxis]
            ret[key] = coords
        return(ret)
        
class ModelView(object):
    def __init__(self,model):
        import copy
        self.model = model
        self.plot_frame = copy.copy(model.frame)
        #self.plot_basis['p'] = default_rframe_data['p']
        #self.plot_basis['a1'] = default_rframe_data['a1']
        #self.plot_basis['a2'] = default_rframe_data['a2']

    def plot(self,plot_frame,plotobject):
        lines = self.model.coords_from_frame(plot_frame)
        self.curves = list()
        for line in lines.values():
            self.curves.append(plotobject.plot(line[0,:],line[1,:]))

    def update_frame(self,plot_frame):
        lines = self.model.coords_from_frame(plot_frame)
        for curve,line in zip(self.curves,lines.values()):
            curve.setData(line[0,:],line[1,:])

    def frame_changed(self,roi):
        pnts = roi.saveState()['points']
        p = np.array(pnts[1])

        a1 = np.array(pnts[0])-p
        a2 = np.array(pnts[2])-p

        self.plot_frame['p'] = p
        self.plot_frame['a1'] = a1
        self.plot_frame['a2'] = a2
        self.update_frame(self.plot_frame)

class ModelViewMPL(ModelView):

    def plot(self,plot_frame,**kwargs):
        import pylab as plb
        default_args = {'plot_frame':True,
                        'frame_head_width':20,
                        'contour_kwargs':{'edgecolor': 'none', 
                                          'linewidth': 0.0, 
                                          'facecolor': 'none'}}
        from pylab import plot,arrow
        lines = self.model.coords_from_frame(plot_frame)
        self.curves = list()
        plot_args = kwargs.pop('plot_args',default_args)

        for line_key in lines.keys():
            try:
                kwargs = plot_args['contour_kwargs'][line_key]
            except KeyError:
                kwargs = default_args['contour_kwargs']
            line = lines[line_key]
            from matplotlib.patches import Polygon
            poly = Polygon(zip(line[0,:],line[1,:]),**kwargs)
            plb.gca().add_patch(poly,)

        if plot_args['plot_frame']:
            p = plot_frame['p']
            a1 = plot_frame['a1']
            a2 = plot_frame['a2']
            kwargs['color'] = 'g'
            kwargs['head_width'] = plot_args['frame_head_width']
            arrow(p[0],p[1],a1[0],a1[1],**kwargs)
            kwargs['color'] = 'b'
            kwargs['head_width'] = plot_args['frame_head_width']
            arrow(p[0],p[1],a2[0],a2[1],**kwargs)


