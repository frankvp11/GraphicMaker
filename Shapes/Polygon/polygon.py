
from nicegui import ui

from nicegui.element import Element

class Polygon(Element, component="polygon.js"):
    def __init__(self, points, fill='red', stroke='red', stroke_width=1):
        super().__init__()
        self.points = points
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self._props['points'] = self.points
        self._props['fill'] = self.fill
        self._props['stroke'] = self.stroke
        self._props['stroke-width'] = self.stroke_width
        
    def set_points(self, points):
        self.points = points
        self._props['points'] = self.points
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
        self.stroke_width = stroke_width
        self._props['stroke-width'] = self.stroke_width
        self.update()
        
