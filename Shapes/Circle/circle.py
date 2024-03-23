

from nicegui import ui

from nicegui.element import Element 


class Circle(Element, component='circle.js'):
    def __init__(self, x, y, radius, **kwargs):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.fill = kwargs.get('fill', 'black')
        self.stroke = kwargs.get('stroke', 'black')
        self.stroke_width = kwargs.get('stroke_width', 1)
        self.x_scale_factor = kwargs.get('x_scale_factor', 1)
        self.y_scale_factor = kwargs.get('y_scale_factor', 1)
        self.rotate_angle = kwargs.get('rotate_angle', 0)
        self.skew_angle_x = kwargs.get('skew_angle_x', 0)
        self.skew_angle_y = kwargs.get('skew_angle_y', 0)
        self.flip_x = kwargs.get('flip_x', False)
        self.flip_y = kwargs.get('flip_y', False)

        self._props['radius'] = self.radius
        self._props['cx'] = self.x
        self._props['cy'] = self.x
        self._props['fill'] = self.fill
        self._props['outline_color'] = self.stroke
        self._props['outline_width'] = self.stroke_width
        self._props['x_scale_factor'] = self.x_scale_factor
        self._props['y_scale_factor'] = self.y_scale_factor
        self._props['rotate_angle'] = self.rotate_angle
        self._props['x_skew_factor'] = self.skew_angle_x
        self._props['y_skew_factor'] = self.skew_angle_y

    def set_outline_color(self, color):
        self.stroke = color
        self._props['outline_color'] = self.stroke
        self.update()


    def set_color(self, color):
        self.fill = color
        self._props['fill'] = self.fill
        self.update()
    
    def set_radius(self, radius):
        self.radius = radius
        self._props['radius'] = self.radius
        self.update()
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
        self._props['cx'] = self.x
        self._props['cy'] = self.y
        self.update()
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self._props['cx'] = self.x
        self._props['cy'] = self.y
        self.update()
    
    def scaleX(self, factor):
        self.radius *= factor
        self._props['radius'] = self.radius
        self.update()
    
    def skewX(self, angle):
        self.skew_angle_x = angle
        self._props['x_skew_factor'] = self.skew_angle_x
        self.update()

    def skewY(self, angle):
        self.skew_angle_y = angle
        self._props['y_skew_factor'] = self.skew_angle_y

        self.update()

    def rotate(self, angle):
        self.rotate_angle = angle
        self._props['rotate_angle'] = self.rotate_angle
        self.update()


    def flipX(self):
        pass
    
    def flipY(self):
        pass

    

        
    
    
        
        