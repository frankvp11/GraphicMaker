
from nicegui import ui

from nicegui.element import Element


class Line(Element, component="line.js"):
    def __init__(self, x1, y1, x2, y2, **kwargs):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
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
        
        self._props['x1'] = self.x1
        self._props['y1'] = self.y1
        self._props['x2'] = self.x2
        self._props['y2'] = self.y2
        self._props['fill'] = self.fill
        self._props['stroke'] = self.stroke
        self._props['stroke_width'] = self.stroke_width
        self._props['x_scale_factor'] = self.x_scale_factor
        self._props['y_scale_factor'] = self.y_scale_factor
        self._props['rotate_angle'] = self.rotate_angle
        self._props['translate_x'] = self.translate_x
        self._props['translate_y'] = self.translate_y
        self._props['x_skew_factor'] = self.x_skew_factor
        self._props['y_skew_factor'] = self.y_skew_factor
        self._props['flip_x'] = self.flip_x
        self._props['flip_y'] = self.flip_y

    def scale(self, factor):
        self.x_scale_factor = factor
        self.y_scale_factor = factor
        self._props['x_scale_factor'] = self.x_scale_factor
        self._props['y_scale_factor'] = self.y_scale_factor
        self.update()
    
    def move(self, x, y):
        self.translate_x = x
        self.translate_y = y
        self._props['translate_x'] = self.translate_x
        self._props['translate_y'] = self.translate_y
        self.update()
    


    def set_x_scale_factor(self, x_scale_factor):
        self.x_scale_factor = x_scale_factor
        self._props['x_scale_factor'] = self.x_scale_factor
        self.update()
    
    def set_y_scale_factor(self, y_scale_factor):
        self.y_scale_factor = y_scale_factor
        self._props['y_scale_factor'] = self.y_scale_factor
        self.update()
    
    def set_rotate_angle(self, rotate_angle):
        self.rotate_angle = rotate_angle
        self.rotate_x = rotate_angle
        self.rotate_y = rotate_angle
        self._props['rotate_angle'] = self.rotate_angle
        self._props['rotate_x'] = self.rotate_x
        self._props['rotate_y'] = self.rotate_y
        self.update()
    
    def set_translate_x(self, translate_x):
        self.translate_x = translate_x
        self._props['translate_x'] = self.translate_x
        self.update()
    
    def set_translate_y(self, translate_y):
        self.translate_y = translate_y
        self._props['translate_y'] = self.translate_y
        self.update()
    
    def set_x_skew_factor(self, x_skew_factor):
        self.x_skew_factor = x_skew_factor
        self._props['x_skew_factor'] = self.x_skew_factor
        self.update()
    
    def set_y_skew_factor(self, y_skew_factor):
        self.y_skew_factor = y_skew_factor
        self._props['y_skew_factor'] = self.y_skew_factor
        self.update()
    
    def set_flip_x(self, flip_x):
        self.flip_x = flip_x
        self._props['flip_x'] = self.flip_x
        self.update()

    def set_flip_y(self, flip_y):
        self.flip_y = flip_y
        self._props['flip_y'] = self.flip_y
        self.update()
    



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