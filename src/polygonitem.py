

from pyqtgraph.graphicsItems.GraphicsObject import *
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph import functions as fn

class PolygonItem(GraphicsObject):
    """
    **Bases:** :class:`GraphicsObject <pyqtgraph.GraphicsObject>`
    
    Item displaying a filled polygon of a 2D points...To align this item correctly with an 
    ImageItem,call isocurve.setParentItem(image)
    """
    

    def __init__(self, data=None, pen='w'):
        """
        Create a new isocurve item. 
        
        ==============  ===============================================================
        **Arguments:**
        data            A 2-dimensional ndarray. Can be initialized as None, and set
                        later using :func:`setData <pyqtgraph.IsocurveItem.setData>`
        pen             The color of the curve item. Can be anything valid for
                        :func:`mkPen <pyqtgraph.mkPen>`
        ==============  ===============================================================
        """
        GraphicsObject.__init__(self)

        self.data = data
        self.path = None
        self.setPen(pen)
        
    
    def setData(self, data):
        """
        Set the data/image to draw isocurves for.
        
        ==============  ========================================================================
        **Arguments:**
        data            A 2-dimensional ndarray.
        level           The cutoff value at which to draw the curve. If level is not specified,
                        the previously set level is used.
        ==============  ========================================================================
        """
        if level is None:
            level = self.level
        self.level = level
        self.data = data
        self.path = None
        self.prepareGeometryChange()
        self.update()
        

    def setLevel(self, level):
        """Set the level at which the isocurve is drawn."""
        self.level = level
        self.path = None
        self.prepareGeometryChange()
        self.update()
    

    def setPen(self, *args, **kwargs):
        """Set the pen used to draw the isocurve. Arguments can be any that are valid 
        for :func:`mkPen <pyqtgraph.mkPen>`"""
        self.pen = fn.mkPen(*args, **kwargs)
        self.update()

    def setBrush(self, *args, **kwargs):
        """Set the brush used to draw the isocurve. Arguments can be any that are valid 
        for :func:`mkBrush <pyqtgraph.mkBrush>`"""
        self.brush = fn.mkBrush(*args, **kwargs)
        self.update()

        
    def updateLines(self, data):
        self.setData(data)

    def boundingRect(self):
        if self.data is None:
            return QtCore.QRectF()
        if self.path is None:
            self.generatePath()
        return self.path.boundingRect()
    
    def generatePath(self):
        if self.data is None:
            self.path = None
            return
        #lines = fn.isocurve(self.data, self.level, connected=True, extendToEdge=True)
        lines = self.data
        self.path = QtGui.QPainterPath()
        for line in lines:
            self.path.moveTo(*line[0])
            for p in line[1:]:
                self.path.lineTo(*p)
    
    def paint(self, p, *args):
        if self.data is None:
            return
        if self.path is None:
            self.generatePath()
        p.setPen(self.pen)
        p.drawPath(self.path)