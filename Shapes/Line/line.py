
from nicegui import ui

from nicegui.element import Element


class Line(Element, component="line.js"):
    def __init__(self, x1, y1, x2, y2, fill='red', stroke='red', stroke_width=1):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self._props['x1'] = self.x1
        self._props['y1'] = self.y1
        self._props['x2'] = self.x2
        self._props['y2'] = self.y2
        self._props['fill'] = self.fill
        self._props['stroke'] = self.stroke
        self._props['stroke_width'] = self.stroke_width
        
    def set_x1(self, x1):
        self.x1 = x1
        self._props['x1'] = self.x1
        self.update()
        
    def set_y1(self, y1):
        self.y1 = y1
        self._props['y1'] = self.y1
        self.update()
        
    def set_x2(self, x2):
        self.x2 = x2
        self._props['x2'] = self.x2
        self.update()
        
    def set_y2(self, y2):
        self.y2 = y2
        self._props['y2'] = self.y2
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