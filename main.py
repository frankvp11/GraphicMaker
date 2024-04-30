
# import math
# from nicegui import ui, app
from .svg import SVG
from .Shapes.AlphaMask.alphamask import AlphaMask
from .Shapes.Circle.circle import Circle
from .Shapes.Clip.clip import Clip
from .Shapes.Group.group import Group
from .Shapes.Line.line import Line
from .Shapes.NGon.ngon import NGon
from .Shapes.Oval.oval import Oval
from .Shapes.Polygon.polygon import Polygon
from .Shapes.Rectangle.rectangle import Rectangle
from .Shapes.Text.text import Text
from .Shapes.PolyLine.polyline import PolyLine


# def main():
#     svg=  SVG().style("border: 1px solid black;")


#     with svg:
#         group = Group()
#         with group:
#             Circle(50, 50, 20, fill="red")
#             Rectangle(100, 100, 50, 50, fill="green")
#             Line(150, 150, 200, 200, stroke="blue", stroke_width=5)
#             NGon(250, 250, 5, 50, fill="yellow")
#         Rectangle(0, 0, 20, 20, fill="black").on("svg:pointerdown", lambda: group.move_group(20, 0))


# main()
# ui.run(on_air=True)
