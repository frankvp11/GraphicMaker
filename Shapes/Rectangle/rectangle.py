
from nicegui import ui
from nicegui.element import Element


class Rectangle(Element, component='rectangle.js'):
    def __init__(self, x, y, width=50, height=50, fill='red', stroke='red', stroke_width=1):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self._props['x'] = self.x
        self._props['y'] = self.y
        self._props['width'] = self.width
        self._props['height'] = self.height
        self._props['fill'] = self.fill
        self._props['stroke'] = self.stroke
        self._props['stroke-width'] = self.stroke_width
        
    def set_x(self, x):
        self.x = x
        self._props['x'] = self.x
        self.update()
        
    def set_y(self, y):
        self.y = y
        self._props['y'] = self.y
        self.update()
        
    def set_width(self, width):
        self.width = width
        self._props['width'] = self.width
        self.update()
        
    def set_height(self, height):
        self.height = height
        self._props['height'] = self.height
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