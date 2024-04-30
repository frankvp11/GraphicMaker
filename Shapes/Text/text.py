
from nicegui import ui
from nicegui.element import Element

class Text(Element, component="text.js"):
    def __init__(self, x, y, text, font_size=20, fill='black', stroke='black', stroke_width=1, centered=False):
        super().__init__()
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self.centered = centered
        self._props['x'] = self.x
        self._props['y'] = self.y
        self._props['text'] = self.text
        self._props['font-size'] = self.font_size
        self._props['fill'] = self.fill
        self._props['stroke'] = self.stroke
        self._props['stroke-width'] = self.stroke_width
        self._props['centered'] = self.centered
        
    def set_x(self, x):
        self.x = x
        self._props['x'] = self.x
        self.update()
        
    def set_y(self, y):
        self.y = y
        self._props['y'] = self.y
        self.update()
        
    def set_text(self, text):
        self.text = text
        self._props['text'] = self.text
        self.update()
        
    def set_font_size(self, font_size):
        self.font_size = font_size
        self._props['font-size'] = self.font_size
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