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
        # Contrast/color control
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.frameView)
        self.ui.frameHist.setCentralItem(self.hist)
        self.current_frame = 0
        self.show()

        ### ROI's
        self.roi_b1 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(1,8))
        self.roi_b1.img = pg.ImageItem()

        self.roi_b2 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(2,8))
        self.roi_b2.img = pg.ImageItem()

        self.roi_b3 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(3,8))
        self.roi_b3.img = pg.ImageItem()

        self.roi_i1 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(4,8))
        self.roi_i1.img = pg.ImageItem()

        self.roi_i2 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(4,8))
        self.roi_i2.img = pg.ImageItem()

        self.roi_iii1 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(5,8))
        self.roi_iii1.img = pg.ImageItem()

        self.roi_iii234 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(6,8))
        self.roi_iii234.img = pg.ImageItem()

        self.roi_hg1 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(7,8))
        self.roi_hg1.img = pg.ImageItem()

        self.roi_hg234 = PolyMaskROI([[0.,0.], [5.,10.],[10.,5.]], closed = True, pen=(8,8))
        self.roi_hg234.img = pg.ImageItem()

        self.view_b1 = pg.PlotWidget()
        self.view_b2 = pg.PlotWidget()
        self.view_b3 = pg.PlotWidget()
        self.view_i1 = pg.PlotWidget()
        self.view_i2 = pg.PlotWidget()
        self.view_iii1 = pg.PlotWidget()
        self.view_iii234 = pg.PlotWidget()
        self.view_hg1 = pg.PlotWidget()
        self.view_hg234 = pg.PlotWidget()

        self.roi_list = [self.roi_b1,
                        self.roi_b2, 
                        self.roi_b3,
                        self.roi_i1,
                        self.roi_i2, 
                        self.roi_iii1, 
                        self.roi_iii234, 
                        self.roi_hg1, 
                        self.roi_hg234]

        self.view_list = [self.view_b1,
                        self.view_b2,
                        self.view_b3,
                        self.view_i1,
                        self.view_i2,
                        self.view_iii1,
                        self.view_iii234,
                        self.view_hg1,
                        self.view_hg234,]


        for i,r,r_view,name in zip(range(len(self.roi_list)),
                                   self.roi_list,
                                   self.view_list,
                                   ['b1','b2','b3','i1','i2','iii1','iii234','hg1','hg234']):
            self.viewb.addItem(r)
            r_view.addItem(r.img)
            r_view.invertY(True)
            r_view.setAspectLocked(True)
            self.roi_layout.addWidget(r_view,i,1,1,1)
            r.sigRegionChanged.connect(self.updateRoi)
            c = self.roi_curves.plot(pen=r.pen)
            r.curve = c
            r.muscle_name = name

        self.muscle_data = dict()
        self.roi_layout.addWidget(self.roi_curves,10,1,1,1)
        self.main_layout.addLayout(self.roi_layout,0,3,7,1)
    
    def updateRoi(self,roi):
        #if roi is None:
        #    return
        sliced_data = roi.getArrayRegion(np.transpose(self.images,[1,2,0]),self.img,axes = (0,1))
        self.updateRoiPlot(roi, sliced_data)


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
        for roi in self.roi_list:
            self.updateRoi(roi)
        #self.thorax_poly.clearPoints()
        #roidata = [(x,y) for x,y in self.thorax_pos[value,:,:]]
        #self.thorax_poly.setPoints(roidata)
        
        #self.basalar_poly.clearPoints()
        #roidata = [(x,y) for x,y in self.basalar_pos[value,:,:]]
        #self.basalar_poly.setPoints(roidata)

        #print value

    def updateRoi(self,roi):
        #if roi is None:
        #    return
        sliced_data = roi.getArrayRegion(np.transpose(self.images,[1,2,0]),self.img,axes = (0,1))
        self.updateRoiPlot(roi, sliced_data)

    def updateRoiPlot(self,roi, data=None):
        if data is None:
            data = roi.getArrayRegion(self.images, img=self.img)
        if data is not None:
            idx = np.squeeze(data[1].astype(int))
            trace = np.sum(np.sum(data[0].astype(float)*idx[:,:,np.newaxis],axis = 0)/(np.sum(idx)),axis=0)
            #trace /= np.mean(trace)
            roi.img.updateImage(data[0][:,:,self.frameNum]*idx[:,:])
            #roi.curve.setData(trace)
            self.muscle_data[roi.muscle_name] = trace

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
