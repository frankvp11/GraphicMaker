
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
    circ = Circle(20, 20, 50, fill='red') \
    .on("svg:pointermove", lambda e : ui.notify("moved on circle 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of circle 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered circle 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on circle 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on circle 1"))

    
ui.run()
