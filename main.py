
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
    # circ = Circle(20, 20, 50, fill='red') \
    # .on("svg:pointermove", lambda e : ui.notify("moved on circle 1")) \
    # .on("svg:pointerout", lambda e : ui.notify("out of circle 1")) \
    # .on("svg:pointerenter", lambda e : ui.notify("entered circle 1")) \
    # .on("svg:pointerdown", lambda e : ui.notify("down on circle 1")) \
    # .on("svg:pointerup", lambda e : ui.notify("up on circle 1"))
    # line = Line(20, 20, 20, 100, fill='red', stroke_width=10, stroke="blue", rotate_angle=10) \
    # .on("svg:pointermove", lambda e : ui.notify("moved on line 1")) \
    # .on("svg:pointerout", lambda e : ui.notify("out of line 1")) \
    # .on("svg:pointerenter", lambda e : ui.notify("entered line 1")) \
    # .on("svg:pointerdown", lambda e : ui.notify("down on line 1")) \
    # .on("svg:pointerup", lambda e : ui.notify("up on line 1"))
    # poly = Polygon([(20, 20), (20, 100), (100, 100), (100, 20)], fill='red', stroke_width=10, stroke="blue", rotate_angle=10, y_skew_factor=10) \
    # .on("svg:pointermove", lambda e : ui.notify("moved on polygon 1")) \
    # .on("svg:pointerout", lambda e : ui.notify("out of polygon 1")) \
    # .on("svg:pointerenter", lambda e : ui.notify("entered polygon 1")) \
    # .on("svg:pointerdown", lambda e : ui.notify("down on polygon 1")) \
    # .on("svg:pointerup", lambda e : ui.notify("up on polygon 1"))
    # NGon1 = NGon(100, 100, 50, sides=3, fill='red', stroke_width=10, stroke="blue", rotate_angle=10, y_skew_factor=10) \
    # .on("svg:pointermove", lambda e : ui.notify("moved on ngon 1")) \
    # .on("svg:pointerout", lambda e : ui.notify("out of ngon 1")) \
    # .on("svg:pointerenter", lambda e : ui.notify("entered ngon 1")) \
    # .on("svg:pointerdown", lambda e : ui.notify("down on ngon 1")) \
    # .on("svg:pointerup", lambda e : ui.notify("up on ngon 1"))



ui.run()
