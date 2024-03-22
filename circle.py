

from nicegui import ui

from nicegui.element import Element 

class Circle(Element, component='circle.js'):
    def __init__(self, x, y, radius=50, fill='red', stroke='red', stroke_width=1):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.fill = fill
        self.stroke = stroke
        self.stroke_width = stroke_width
        self._props['radius'] = self.radius
        self._props['cx'] = self.x
        self._props['cy'] = self.x
        

        # self.update()
        
    
    
        
        