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
tiff_file = '/media/FlyDataB/FlyDB/Fly0212/T2_trial1_ND_04_1ms_exposure/T2_trial1_ND_04_1ms_exposure_MMStack.ome.tif'


i1 =        [[92.50577788    ,91.0009609 ],
            [ 102.93406073   ,85.20281021],
            [ 115.4942443    ,64.00148121],
            [  74.70869468   ,73.21371393],
            [  67.46997482  ,120.31315518],
            [  70.73564502  ,121.59745963]]

i2 =        [[  87.23880877  ,117.43773222],
            [ 115.73328887   ,63.65810097],
            [ 113.99450968   ,46.65826797],
            [  37.49521187   ,73.21371393],
            [  14.17115114  ,100.75790925],
            [  50.93048632  ,126.14644604]]


class MainWindow(TemplateBaseClass):  
    def __init__(self):
        TemplateBaseClass.__init__(self)
        self.setWindowTitle('pyqtgraph example: Qt Designer')
        
        # Create the main window
        self.ui = WindowTemplate()
        self.ui.setupUi(self)
        #frame view
        self.vb = pg.ViewBox()
        self.vb.setAspectLocked()
        self.ui.frameView.setCentralItem(self.vb)
        self.frameView = pg.ImageItem()
        self.vb.addItem(self.frameView)
        #load frames button
        self.ui.loadFrames.clicked.connect(self.loadFrames)
        #save data button
        self.ui.saveTracks.clicked.connect(self.saveTracks)
        self.ui.loadTracks.clicked.connect(self.loadTracks)

        ##scroll bar
        self.ui.frameScrollBar.valueChanged.connect(self.frameScrollBar_valueChanged)

        ### ROI's
        #int_pnt = [14.171640, 5.061034]
        int_pnt = (0, 0)
        self.i1_init = i1
        self.i1_init = [[x+int_pnt[0],y+int_pnt[1]] for x,y in self.i1_init]

        self.i2_init = i2
        self.i2_init = [[x+int_pnt[0],y+int_pnt[1]] for x,y in self.i2_init]
        

        self.thorax_poly = PolyMaskROI(self.i1_init, closed = True, pen=(1,6))
        self.basalar_poly = PolyMaskROI(self.i2_init, closed = True, pen=(1,3))
        
        self.thorax_pos = np.zeros((1000,np.shape(self.i1_init)[0],np.shape(self.i1_init)[1]))
        self.thorax_pos[:,:,:] = np.array(self.i1_init)[np.newaxis,:,:]

        self.basalar_pos = np.zeros((1000,np.shape(self.i2_init)[0],np.shape(self.i2_init)[1]))
        self.basalar_pos[:,:,:] = np.array(self.i2_init)[np.newaxis,:,:]

        self.vb.addItem(self.thorax_poly)
        self.thorax_poly.sigRegionChanged.connect(self.poly_state_change)

        self.vb.addItem(self.basalar_poly)
        self.basalar_poly.sigRegionChanged.connect(self.poly_state_change)

        # Contrast/color control
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.frameView)
        self.ui.frameHist.setCentralItem(self.hist)

        self.current_frame = 0
        self.show()

    def loadFrames(self):
        tif = tifffile.TiffFile(tiff_file)
        self.images = tif.asarray()
        self.frameView.setImage(self.images[0,:,:])
        self.ui.frameScrollBar.setMaximum(np.shape(self.images)[0])
        
        self.thorax_pos = np.zeros((np.shape(self.images)[0],np.shape(self.i1_init)[0],np.shape(self.i1_init)[1]))
        self.thorax_pos[:,:,:] = np.array(self.i1_init)[np.newaxis,:,:]

        
        self.basalar_pos = np.zeros((np.shape(self.images)[0],np.shape(self.i2_init)[0],np.shape(self.i2_init)[1]))
        self.basalar_pos[:,:,:] = np.array(self.i2_init)[np.newaxis,:,:]


    def frameScrollBar_valueChanged(self,value):
        self.frameView.setImage(self.images[value,:,:])
        self.current_frame = value
        
        self.thorax_poly.clearPoints()
        roidata = [(x,y) for x,y in self.thorax_pos[value,:,:]]
        self.thorax_poly.setPoints(roidata)
        
        self.basalar_poly.clearPoints()
        roidata = [(x,y) for x,y in self.basalar_pos[value,:,:]]
        self.basalar_poly.setPoints(roidata)
        print value

    def poly_state_change(self):
        #print [tuple(h.pos()) for h in self.thorax_poly.getHandles()]
        #print self.thorax_poly.getSceneHandlePositions()
        #print self.thorax_poly.pos()
        #print self.thorax_poly.mapHandlesInImage(self.frameView)
        roidata = np.array(self.thorax_poly.mapHandlesInImage(self.frameView))
        #print roidata
        self.thorax_pos[self.current_frame,:,:] = roidata
        roidata = np.array(self.basalar_poly.mapHandlesInImage(self.frameView))
        #print roidata
        self.basalar_pos[self.current_frame,:,:] = roidata
        #print np.shape(roidata)
        #print np.shape(self.poly_array)

    def saveTracks(self):
        import cPickle
        f = open('roi_tracks.cpkl','wb')
        cPickle.dump({'basalar':self.basalar_pos,'thorax':self.thorax_pos},f)
        f.close()

    def loadTracks(self):
        import cPickle
        f = open('roi_tracks.cpkl','rb')
        roidata = cPickle.load(f)
        f.close()
        self.basalar_pos = roidata['basalar']
        self.thorax_pos = roidata['thorax']

class PolyMaskROI(pg.PolyLineROI):
    def getArrayRegion(self, data, img, axes=(0,1), returnMappedCoords=False, **kwds):
        import pyqtgraph.functions as fn
        sl = self.getArraySlice(data, img, axes=(0,1))
        if sl is None:
            return None
        sliced = data[sl[0]]
        im = QtGui.QImage(sliced.shape[axes[0]], sliced.shape[axes[1]], QtGui.QImage.Format_ARGB32)
        im.fill(0x0)
        p = QtGui.QPainter(im)
        p.setPen(fn.mkPen(None))
        p.setBrush(fn.mkBrush('w'))
        p.setTransform(self.itemTransform(img)[0])
        bounds = self.mapRectToItem(img, self.boundingRect())
        p.translate(-bounds.left(), -bounds.top()) 
        p.drawPath(self.shape())
        p.end()
        
        mask = fn.imageToArray(im)[:,:,0].astype(float) / 255.
        shape = [1] * data.ndim
        shape[axes[0]] = sliced.shape[axes[0]]
        shape[axes[1]] = sliced.shape[axes[1]]
        return sliced, mask.reshape(shape)

    def mapHandlesInImage(self,img):
        orig = self.pos()
        hcoords = [tuple(h.pos()) for h in self.getHandles()]
        return [[x+orig[0],y+orig[1]] for x,y in hcoords]
        #bounds = self.mapRectToItem(img, self.boundingRect())
        #img_origin = [bounds.left(),bounds.top()]
        #print img_origin
        #hpos = [h['item'].pos() for h in self.handles]
        #return [(img_origin[0]+h[1],img_origin[1]+h[0]) for h in hpos]

win = MainWindow()


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
