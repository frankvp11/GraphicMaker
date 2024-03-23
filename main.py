
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

svg=  SVG().style("border: 1px solid black;")





with svg:

    # Circle(50, 50, 50)
    # Rectangle(50, 50, 100, 100, stroke_width=10, stroke="blue").on("svg:pointerdown", lambda: print("Rectangle clicked"))


ui.run()
