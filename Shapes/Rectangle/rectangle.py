
from nicegui import ui
from nicegui.element import Element


class Rectangle(Element, component='rectangle.js'):
    def __init__(self, x, y, width=50, height=50, **kwargs):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fill = kwargs.get('fill', 'black')
        self.stroke = kwargs.get('stroke', 'black')
        self.stroke_width = kwargs.get('stroke_width', 1)
        self.x_scale_factor = kwargs.get('x_scale_factor', 1)
        self.y_scale_factor = kwargs.get('y_scale_factor', 1)
        self.rotate_angle = kwargs.get('rotate_angle', 0)
        self.rotate_x = self.rotate_angle
        self.rotate_y = self.rotate_angle
        self.translate_x = kwargs.get('translate_x', 0)
        self.translate_y = kwargs.get('translate_y', 0)
        self.x_skew_factor = kwargs.get('x_skew_factor', 0)
        self.y_skew_factor = kwargs.get('y_skew_factor', 0)
        self.flip_x = kwargs.get('flip_x', False)
        self.flip_y = kwargs.get('flip_y', False)
        self._props['x'] = self.x
        self._props['y'] = self.y
        self._props['width'] = self.width
        self._props['height'] = self.height
        self._props['fill'] = self.fill
        self._props['outline_color'] = self.stroke
        self._props['outline_width'] = self.stroke_width
        self._props['x_scale_factor'] = self.x_scale_factor
        self._props['y_scale_factor'] = self.y_scale_factor
        self._props['rotate_angle'] = self.rotate_angle
        self._props['translate_x'] = self.translate_x
        self._props['translate_y'] = self.translate_y
        self._props['x_skew_factor'] = self.x_skew_factor
        self._props['y_skew_factor'] = self.y_skew_factor
        self._props['flip_x'] = self.flip_x
        self._props['flip_y'] = self.flip_y



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

    def __str__(self, indent : int = 0) -> str:
        return "  " * indent + f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height}, fill='{self.fill}', stroke='{self.stroke}', stroke_width={self.stroke_width})\n"
    
