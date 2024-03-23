
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
    with clip:
        rect = Rectangle(0, 0, 100, 100, fill='blue')
        circ = Circle(50, 50, 50, fill='red')


ui.run()
