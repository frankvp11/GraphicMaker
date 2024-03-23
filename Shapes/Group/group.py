
from nicegui.element import Element


class Group(Element, component="group.js"):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self._props = {"x": self.x, "y": self.y}
    
    def move_group(self, x: int, y: int) -> None:
        print("move_group")
        previous_x = self._props["x"]
        previous_y = self._props["y"]
        self._props["x"] = x + previous_x
        self._props["y"] = previous_y + y
        self.update()
