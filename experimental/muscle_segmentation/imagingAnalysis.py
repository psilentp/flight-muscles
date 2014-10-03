# -*- coding: utf-8 -*-
"""
Simple example of loading UI template created with Qt Designer.

This example uses uic.loadUiType to parse and load the ui at runtime. It is also
possible to pre-compile the .ui file using pyuic (see VideoSpeedTest and 
ScatterPlotSpeedTest examples; these .ui files have been compiled with the
tools/rebuildUi.py script).
"""
#import initExample ## Add path to library (just for examples; you do not need this)

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import os

pg.mkQApp()

## Define main window class from template
path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(path, 'imagingAnalysis.ui')
WindowTemplate, TemplateBaseClass = pg.Qt.loadUiType(uiFile)

import tifffile
import numpy as np
#tiff_file = '/volumes/FlyDataB/FlyDB/Fly0212/T2_trial1_ND_04_1ms_exposure/T2_trial1_ND_04_1ms_exposure_MMStack.ome.tif'

tiff_file_name = '/Volumes/FlyDataB/FlyDB/Fly0267/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif'

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
    def __init__(self,lines,basis):
        self.lines = lines
        self.basis = basis
        ## put lines in barycentric coords
        self.barycentric = dict()
        for key in self.lines.keys():
            coords = np.dot(self.basis['A_inv'],(self.lines[key]-self.basis['p'][:,np.newaxis])) 
            self.barycentric[key] = coords.T
            
    def coords_from_basis(self,basis):
        ret = dict()
        for key in self.barycentric.keys():
            coords = np.dot(basis['A'],(self.barycentric[key]).T)+basis['p'][:,np.newaxis]
            ret[key] = coords
        return(ret)
        
class ModelView(object):
    def __init__(self,model):
        import copy
        self.model = model
        self.plot_basis = copy.copy(model.basis)
        
    def plot(self,basis,plotobject):
        lines = self.model.coords_from_basis(basis)
        self.curves = list()
        for line in lines.values():
            self.curves.append(plotobject.plot(line[0,:],line[1,:]))

    def update_basis(self,basis):
        lines = self.model.coords_from_basis(basis)
        for curve,line in zip(self.curves,lines.values()):
            curve.setData(line[0,:],line[1,:])

    def basis_changed(self,roi):
        pnts = roi.saveState()['points']
        p = np.array(pnts[1])

        a1 = np.array(pnts[0])-p
        a2 = np.array(pnts[2])-p

        self.plot_basis['p'] = p
        self.plot_basis['a1'] = a1
        self.plot_basis['a2'] = a2
        self.update_basis(self.plot_basis)



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



class MainWindow(TemplateBaseClass):  
    def __init__(self):
        TemplateBaseClass.__init__(self)
        self.setWindowTitle('pyqtgraph example: Qt Designer')
        
        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)
        #frame view
        #self.vb = pg.ViewBox()
        #self.vb.setAspectLocked()
        self.plt = pg.PlotItem()
        self.ui.frameView.setCentralItem(self.plt)
        self.frameView = pg.ImageItem()
        #self.plt = pg.PlotItem()
        self.plt.addItem(self.frameView)
        #self.vb.addItem(self.plt)
        
        #load frames button
        self.ui.loadFrames.clicked.connect(self.loadFrames)
        #save data button
        self.ui.saveTracks.clicked.connect(self.saveTracks)
        self.ui.loadTracks.clicked.connect(self.loadTracks)

        ##scroll bar
        self.ui.frameScrollBar.valueChanged.connect(self.frameScrollBar_valueChanged)

        # Contrast/color control
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.frameView)
        self.ui.frameHist.setCentralItem(self.hist)

        #load data
        self.loadData()
        self.current_frame = 0
        self.show()

    def loadData(self):
        import cPickle
        f = open('model_data.cpkl','rb')
        model_data = cPickle.load(f)
        f.close()

        imfile = tifffile.TiffFile('test_imgdata.tiff')
        sumimg = imfile.asarray()


        ########################
        #model_keys = []
        e1 = model_data['e1']
        e2 = model_data['e2']

        muscle_dict = dict()
        for key in model_data.keys():
            if not(key in ['e1','e2']):
                muscle_dict[key] = model_data[key]
        basis = Basis()
        basis['a2'] = e1[1]-e2[0]
        basis['a1'] = e2[1]-e2[0]
        basis['p'] = e2[0]
        thorax = GeometricModel(muscle_dict,basis)
        self.thorax_view = ModelView(thorax)
        roi = BasisROI(thorax.basis)
        roi.sigRegionChanged.connect(self.thorax_view.basis_changed)

        self.plt.disableAutoRange('xy')

        self.plt.addItem(roi)
        self.thorax_view.plot(self.thorax_view.plot_basis,self.plt)


    def loadFrames(self):
        tif = tifffile.TiffFile(tiff_file_name)
        self.images = tif.asarray()
        self.frameView.setImage(self.images[0,:,:])
        self.ui.frameScrollBar.setMaximum(np.shape(self.images)[0])
        self.plt.autoRange()


    def frameScrollBar_valueChanged(self,value):
        self.frameView.setImage(self.images[value,:,:])
        self.current_frame = value
        

    def saveTracks(self):
        pass


    def loadTracks(self):
        pass


win = MainWindow()


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
