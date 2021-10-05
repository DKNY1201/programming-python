from OOP.State.Tool import Tool


class BrushTool(Tool):
    def select(self):
        print("Brush icon")

    def draw(self):
        print("Line")