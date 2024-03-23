
import math
from nicegui import ui
from svg import SVG
from Shapes.AlphaMask.alphamask import AlphaMask
from Shapes.Circle.circle import Circle
from Shapes.Polygon.polygon import Polygon
from Shapes.Rectangle.rectangle import Rectangle
from Shapes.Line.line import Line
from Shapes.NGon.ngon import NGon
from Shapes.Oval.oval import Oval
from Shapes.Text.text import Text
from Shapes.Clip.clip import Clip
from Shapes.Group.group import Group

svg=  SVG().style("border: 1px solid black;")

with svg:
    group = Group()
    with group:
        Circle(50, 50, 20, fill="red")
        Rectangle(100, 100, 50, 50, fill="green")
        Line(150, 150, 200, 200, stroke="blue", stroke_width=5)
        NGon(250, 250, 5, 50, fill="yellow")
    # group.move_group(20, 0)
    Rectangle(0, 0, 20, 20, fill="black").on("svg:pointerdown", lambda: group.move_group(20, 0))


ui.run()
