

from nicegui.element import Element


class SVG(Element, component="svg.js"):
    def __init__(self, width: int = 200, height: int = 200) -> None:
        super().__init__()
        self.width = width
        self.height = height

        self._props['width'] = width
        self._props['height'] = height
        
        

