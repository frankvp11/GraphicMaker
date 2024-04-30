

from nicegui.element import Element


class SVG(Element, component="svg.js"):
    def __init__(self, width: int = 200, height: int = 200) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.children = []

        self._props['width'] = width
        self._props['height'] = height
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_children(self, children):
        self.children.extend(children)

