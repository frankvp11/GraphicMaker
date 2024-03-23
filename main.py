

from nicegui import ui
from svg import SVG
from Shapes.Circle.circle import Circle
from Shapes.Polygon.polygon import Polygon
from Shapes.Rectangle.rectangle import Rectangle
from Shapes.Line.line import Line
from Shapes.NGon.ngon import NGon
from Shapes.Oval.oval import Oval
from Shapes.Text.text import Text

svg=  SVG()

with svg:
    Circle(100, 100, 50, fill='red') \
    .on("svg:pointermove", lambda e : ui.notify("moved on circle 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of circle 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered circle 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on circle 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on circle 1"))
    Polygon([(10, 10), (20, 20), (10, 30)], fill='yellow') \
    .on("svg:pointermove", lambda e : ui.notify("moved on polygon 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of polygon 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered polygon 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on polygon 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on polygon 1"))

    Rectangle(100, 0, 50, 50, fill='blue') \
    .on("svg:pointermove", lambda e : ui.notify("moved on rectangle 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of rectangle 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered rectangle 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on rectangle 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on rectangle 1"))
    
    line = Line(0, 0, 100, 100, fill='green') \
    .on("svg:pointermove", lambda e : ui.notify("moved on line 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of line 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered line 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on line 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on line 1"))
    line.set_stroke_width(10)
    
    NGon(100, 50, 20, sides=5) \
    .on("svg:pointermove", lambda e : ui.notify("moved on ngon 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of ngon 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered ngon 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on ngon 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on ngon 1"))

    Oval(20, 100, 20, 12, fill='purple') \
    .on("svg:pointermove", lambda e : ui.notify("moved on oval 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of oval 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered oval 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on oval 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on oval 1"))
    


    Text(100, 100, "Hello World", fill='black') \
    .on("svg:pointermove", lambda e : ui.notify("moved on text 1")) \
    .on("svg:pointerout", lambda e : ui.notify("out of text 1")) \
    .on("svg:pointerenter", lambda e : ui.notify("entered text 1")) \
    .on("svg:pointerdown", lambda e : ui.notify("down on text 1")) \
    .on("svg:pointerup", lambda e : ui.notify("up on text 1"))
    

ui.run()
