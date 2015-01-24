##Library for aligning muscle models to the thorax of the fly

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
            
    def coords_from_frame(self,frame):
        ret = dict()
        for key in self.barycentric.keys():
            coords = np.dot(frame['A'],(self.barycentric[key]).T)+frame['p'][:,np.newaxis]
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
        
    def plot(self,frame,plotobject):
        lines = self.model.coords_from_frame(frame)
        self.curves = list()
        for line in lines.values():
            self.curves.append(plotobject.plot(line[0,:],line[1,:]))

    def update_frame(self,frame):
        lines = self.model.coords_from_frame(frame)
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