from OOP.State.Canvas import Canvas
from OOP.State.BrushTool import BrushTool
from OOP.State.SelectionTool import SelectionTool
from OOP.State.EraseTool import EraseTool


canvas = Canvas()

canvas.setTool(BrushTool())
canvas.select()
canvas.draw()

canvas.setTool(SelectionTool())
canvas.select()
canvas.draw()

canvas.setTool(EraseTool())
canvas.select()
canvas.draw()