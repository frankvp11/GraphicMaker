
from nicegui import ui
from nicegui.element import Element


class Oval(Element, component="oval.js"):
    def __init__(self, x, y, rx=50, ry=50, fill='red', stroke='red', stroke_width=1):
        super().__init__()
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self._props['rx'] = self.rx
        self._props['ry'] = self.ry
        self._props['cx'] = self.x
        self._props['cy'] = self.y
        self._props['fill'] = self.fill
        self._props['stroke'] = self.stroke
        self._props['stroke-width'] = self.stroke_width
        
    def set_x(self, x):
        self.x = x
        self._props['cx'] = self.x
        self.update()
        
    def set_y(self, y):
        self.y = y
        self._props['cy'] = self.y
        self.update()
        
    def set_rx(self, rx):
        self.rx = rx
        self._props['rx'] = self.rx
        self.update()
        
    def set_ry(self, ry):
        self.ry = ry
        self._props['ry'] = self.ry
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

    def __str__(self, indent : int = 0) -> str:
        return "  " * indent + f"Oval({self.x}, {self.y},rx={self.rx}, ry={self.ry}, fill='{self.fill}', stroke='{self.stroke}', stroke_width={self.stroke_width})\n"