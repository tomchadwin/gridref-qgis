import urllib
from qgis.gui import *
from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class PointTool(QgsMapTool):
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        
        

    def canvasPressEvent(self, event):
        pass

    def canvasMoveEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()

        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        

    def canvasReleaseEvent(self, event):
        #Get the click
        x = event.pos().x()
        y = event.pos().y()
        
        espg = self.canvas.mapRenderer().destinationCrs().authid()
        bbox = QgsRectangle(4999.99,4999.69,660000.06,1225000.12)
        
        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        coords = point.toString ()
        f = urllib.urlopen("http://gridref.longwayaround.org.uk/convert/%s?figures=4" % coords)
        f.geturl() # Prints the final URL with parameters.
        gridref = f.read() # Prints the contents
        os_ref = gridref[12:18]
        print os_ref
        #if espg == '27700':
        if bbox.contains(point):
            QMessageBox.information(None,"Info", "Grid Ref: " + os_ref)
        else:
            QMessageBox.information(None,"Error", "Point out of bounds")
        #print espg
        #print bbox.toString()
    
        
        
        
