

from nicegui.element import Element


class SVG(Element, component="svg.js"):
    def __init__(self, width: int = 200, height: int = 200, viewBox : dict = {"x":0, "y":0, "width":200, "height":200}) -> None:
        super().__init__()
        self.width = width
        self.height = height
        self.viewBox = viewBox
        self.children = []
        self._props['width'] = width
        self._props['height'] = height
        self._props['viewBox'] = " ".join(([str(val) for val in viewBox.values()]))
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_children(self, children):
        self.children.extend(children)
    
    def __str__(self) -> str:
        code = "svg = SVG(width={}, height={}, viewBox={})\n".format(self.width, self.height, self.viewBox)
        code += "with svg:\n"
        for child in self.children:
            # code += str(child)
            code += child.__str__(indent=1)
        return code
    
