

from nicegui import ui
from svg import SVG
from circle import Circle

svg=  SVG()

with svg:
    Circle(100, 100, 50, fill='red').on("svg:pointermove", lambda e : ui.notify("moved on circle 1"))
    Circle(180, 180, 50, fill='green').on("svg:pointermove", lambda e : ui.notify("moved on circle 2"))
    Circle(10, 10, 50, fill='blue').on("svg:pointermove", lambda e : ui.notify("moved on circle 3"))


ui.run()
