from OOP.Memento.Editor import Editor
from OOP.Memento.History import History
from OOP.Memento.EditorState import EditorState

editor = Editor()
history = History()

editor.setContent('a')
editor.setTitle('Memento')
history.push(EditorState(editor.getContent(), editor.getTittle()))
editor.setContent('ab')
editor.setTitle('Memento111')
editor.setTitle('Memento1')
history.push(EditorState(editor.getContent(), editor.getTittle()))
editor.setContent('abc')
editor.setTitle('Memento_101')

print(editor)
editor.restore(history.pop())
print(editor)
editor.restore(history.pop())
print(editor)