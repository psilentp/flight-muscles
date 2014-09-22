
import tifffile
from pylab import *
import numpy as np



class Basis(dict):    
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
        self.basis = basis
        ## put lines in barycentric coords
        self.barycentric = dict()
        for key in self.lines.keys():
            coords = dot(self.basis['A_inv'],(self.lines[key]-self.basis['p']).T) 
            self.barycentric[key] = coords.T
            
    def coords_from_basis(self,basis):
        ret = dict()
        for key in self.barycentric.keys():
            coords = np.dot(basis['A'],(self.barycentric[key].T)).T+basis['p']
            ret[key] = coords
        return(ret)
        
    def get_H_from_basis(self,in_basis,out_basis):
        Vin = np.vstack([in_basis['a1'],in_basis['a2']])
        Vout = np.vstack([out_basis['a1'],out_basis['a2']])
        H = np.dot(Vout,np.linalg.inv(Vin))
        return H

class ModelView(object):
    def __init__(self,model):
        self.model = model
        
    def plot(self,basis,plotobject):
        lines = self.model.coords_from_basis(basis)
        self.curves = list()
        for line in lines.values():
            self.curves.append(plotobject.plot(line[:,0],line[:,1]))

    def update_basis(self,basis):
        lines = self.model.coords_from_basis(basis)
        for curve,line in zip(self.curves,lines.values()):
            curve.setData(line[:,0],line[:,1])

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

class BasisROI(pg.ROI):
    
    def __init__(self, basis, closed=False, pos=None, **args):
        
        pos = [0,0]
        
        self.closed = closed
        self.segments = []
        pg.ROI.__init__(self, pos, **args)
        
        self.addFreeHandle((basis['p'][0]+basis['a1'][0],basis['p'][1]+basis['a1'][1]))
        self.addFreeHandle((basis['p'][0],basis['p'][1]))
        self.addFreeHandle((basis['p'][0]+basis['a2'][0],basis['p'][1]+basis['a2'][1]))
        for i in range(0, len(self.handles)-1):
            self.addSegment(self.handles[i]['item'], self.handles[i+1]['item'])
            
    def addSegment(self, h1, h2, index=None):
        seg = pg.LineSegmentROI(handles=(h1, h2), pen=self.pen, parent=self, movable=False)
        if index is None:
            self.segments.append(seg)
        else:
            self.segments.insert(index, seg)
        #seg.sigClicked.connect(self.segmentClicked)
        #seg.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
        seg.setZValue(self.zValue()+1)
        for h in seg.handles:
            h['item'].setDeletable(False)
        
    def saveState(self):
        state = pg.ROI.saveState(self)
        state['closed'] = self.closed
        state['points'] = [tuple(h.pos()) for h in self.getHandles()]
        return state


import cPickle
f = open('model_data.cpkl','rb')
model_data = cPickle.load(f)
f.close()

imfile = tifffile.TiffFile('test_imgdata.tiff')
sumimg = imfile.asarray()
#imshow(sumimg)
e1 = model_data['e1']
e2 = model_data['e2']

muscle_dict = dict()
for key in model_data.keys():
    if not(key in ['e1','e2']):
        muscle_dict[key] = model_data[key]

i1 = model_data['i1']
iii3 = model_data['iii3']
i2 = model_data['i2']

basis = Basis()
basis['a1'] = e1[1]-e2[0]
basis['a2'] = e2[1]-e2[0]
basis['p'] = e2[0]

thorax = GeometricModel(muscle_dict,basis)
thorax_view = ModelView(thorax)

app = QtGui.QApplication([])
#img = pg.ImageItem(np.transpose(sumimg,(1,0,2)))
img = pg.ImageItem(sumimg)
plt = pg.plot()
plt.addItem(img)
img.setZValue(-100) 
roi = BasisROI(thorax.basis)
plt.addItem(roi)
plt.disableAutoRange('xy')
plt.autoRange()

import copy
plot_basis = copy.copy(thorax.basis)
thorax_view.plot(plot_basis,plt)

def basis_changed(roi):
    pnts = roi.saveState()['points']
    p = np.array(pnts[1])
    a1 = np.array(pnts[0])-p
    a2 = np.array(pnts[2])-p
    plot_basis['p'] = p
    plot_basis['a1'] = a1
    plot_basis['a2'] = a2
    thorax_view.update_basis(plot_basis)


roi.sigRegionChanged.connect(basis_changed)


if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

f = open('plot_basis.cpkl','wb')
cPickle.dump(dict(plot_basis),f)
f.close()