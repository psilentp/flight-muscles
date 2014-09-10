import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

class ImagingViewer(object):
    def __init__(self,expmnt):
        self.images = expmnt.get_images()
        self.app = QtGui.QApplication([])
        self.w = QtGui.QWidget()
        self.main_layout = QtGui.QGridLayout()
        self.w.setLayout(self.main_layout)
        #####
        self.sldr = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sldr.valueChanged[int].connect(self.sldr_value_changed_clbk)
        self.sldr.setMinimum(0)
        self.sldr.setMaximum(np.shape(self.images)[0])
        #####
        self.viewb = pg.PlotWidget()
        self.viewb.invertY(True)
        self.viewb.setAspectLocked(True)
        #####
        self.img = pg.ImageItem(self.images[0,:,:],autoLevels = False,levels = (0,60))
        self.viewb.addItem(self.img)
        self.viewb.setRange(QtCore.QRectF(0, 0, 200, 120))
        #####

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
            
        self.main_layout.addWidget(self.viewb,0,0,7,2)
        self.main_layout.addWidget(self.sldr,8,0,1,3)

        self.roi_layout = QtGui.QGridLayout()


        self.view_b1 = pg.PlotWidget()
        self.view_b2 = pg.PlotWidget()
        self.view_b3 = pg.PlotWidget()
        self.view_i1 = pg.PlotWidget()
        self.view_i2 = pg.PlotWidget()
        self.view_iii1 = pg.PlotWidget()
        self.view_iii234 = pg.PlotWidget()
        self.view_hg1 = pg.PlotWidget()
        self.view_hg234 = pg.PlotWidget()
        self.roi_curves = pg.PlotWidget()

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

    def run(self):
        self.w.show()
        self.app.exec_()
    
    def sldr_value_changed_clbk(self,value):
        self.frameNum = value
        self.img.updateImage(self.images[value,:,:])
        for roi in self.roi_list:
            self.updateRoi(roi)
    
    def updateRoi(self,roi):
        #if roi is None:
        #    return
        sliced_data = roi.getArrayRegion(np.transpose(self.images,[1,2,0]),self.img,axes = (0,1))
        self.updateRoiPlot(roi, sliced_data)
    
    def updateRoiPlot(self,roi, data=None):
        pass
        if data is None:
            data = roi.getArrayRegion(self.images, img=self.img)
        if data is not None:
            idx = np.squeeze(data[1].astype(int))
            trace = np.sum(np.sum(data[0].astype(float)*idx[:,:,np.newaxis],axis = 0)/(np.sum(idx)),axis=0)
            #trace /= np.mean(trace)
            roi.img.updateImage(data[0][:,:,self.frameNum]*idx[:,:])
            roi.curve.setData(trace)
            self.muscle_data[roi.muscle_name] = trace
            

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



