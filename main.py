
import math
from nicegui import ui
from svg import SVG
from Shapes.Circle.circle import Circle
from Shapes.Polygon.polygon import Polygon
from Shapes.Rectangle.rectangle import Rectangle
from Shapes.Line.line import Line
from Shapes.NGon.ngon import NGon
from Shapes.Oval.oval import Oval
from Shapes.Text.text import Text
from Shapes.Clip.clip import Clip

svg=  SVG().style("border: 1px solid black;")







with svg:
    clip = Clip()
    with clip.add_slot("maskShape"):
        Rectangle(50, 50, 100, 100)
    with clip.add_slot("maskedShape"):
        Circle(50,50,50)
    Circle(100, 100, 25, fill="red")
        
        

ui.run()
