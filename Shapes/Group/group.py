
from nicegui.element import Element


class Group(Element, component="group.js"):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self._props = {"x": self.x, "y": self.y}
        self.children = []
    
    def move_group(self, x: int, y: int) -> None:
        print("move_group")
        previous_x = self._props["x"]
        previous_y = self._props["y"]
        self._props["x"] = x + previous_x
        self._props["y"] = previous_y + y
        self.update()
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_children(self, children):
        self.children.extend(children)
    
    def __str__(self, indent: int = 0) -> str:
        code = "  " * indent + "group = Group(x={}, y={})\n".format(self.x, self.y)
        code += "  " * indent + "with group:\n"
        for child in self.children:
            code += "  " * indent + child.__str__(indent=indent + 1)
        return code
    

