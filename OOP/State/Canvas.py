class Canvas:
    def setTool(self, tool):
        self.tool = tool

    def getTool(self):
        return self.tool

    def select(self):
        self.tool.select()

    def draw(self):
        self.tool.draw()