from OOP.State.Tool import Tool


class SelectionTool(Tool):
    def select(self):
        print("Selection icon")

    def draw(self):
        print("Dash rectangle")