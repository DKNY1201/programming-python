from OOP.State.Tool import Tool


class EraseTool(Tool):
    def select(self):
        print("Eraser icon")

    def draw(self):
        print("Erase something")