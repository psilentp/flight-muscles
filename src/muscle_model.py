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
                        
class GeometricModel(object):   
    def __init__(self,lines,frame):
        self.lines = lines
        self.frame = frame
        ## put lines in barycentric coords
        self.barycentric = dict()
        for key in self.lines.keys():
            coords = np.dot(self.frame['A_inv'],(self.lines[key]-self.frame['p'][:,np.newaxis])) 
            self.barycentric[key] = coords.T
            
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
        from pylab import plot,arrow
        lines = self.model.coords_from_frame(plot_frame)
        self.curves = list()
        plot_args = {}
        plot_args['plot_frame'] = kwargs.pop('plot_frame',True)
        plot_args['frame_head_width'] = kwargs.pop('frame_head_width',20)
        plot_args['contour_color'] = kwargs.pop('contour_color','w')
        
        kwargs['color'] = plot_args['contour_color']
        for line in lines.values():
            plot(line[0,:],line[1,:], **kwargs)
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