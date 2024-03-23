
from nicegui import ui
from nicegui.element import Element
import math
from ..Polygon.polygon import Polygon


class NGon(Polygon):
    def __init__(self, x, y, radius, sides=3, **kwargs):
        self.x = x
        self.y = y
        self.radius = radius
        self.sides = sides
        super().__init__(points=self.get_points(), **kwargs)

        
    def get_points(self):
        points = []
        for i in range(self.sides):
            angle = 2 * 3.14159265359 * i / self.sides
            x = self.x + self.radius * math.cos(angle)
            y = self.y + self.radius * math.sin(angle)
            points.append((x, y))
        return points

    def set_x(self, x):
        self.x = x
        self._props['cx'] = self.x
        self._props['points'] = self.get_points()
        self.update()
        
    def set_y(self, y):
        self.y = y
        self._props['cy'] = self.y
        self._props['points'] = self.get_points()
        self.update()
        
    def set_radius(self, radius):
        self.radius = radius
        self._props['radius'] = self.radius
        self._props['points'] = self.get_points()
        self.update()
        
    def set_sides(self, sides):
        self.sides = sides
        self._props['sides'] = self.sides
        self._props['points'] = self.get_points()
        self.update()
        
    def set_fill(self, fill):
        self.fill = fill
        self._props['fill'] = self.fill
        self.update()
        
    def set_stroke(self, stroke):
        self.stroke = stroke
        self._props['stroke'] = self.stroke
        self.update()
        
    def set_stroke_width(self, stroke_width):
        self.stroke
