from OOP.Memento.EditorState import EditorState

class Editor:
    def setContent(self, content):
        self.__content = content

    def getContent(self):
        return self.__content

    def setTitle(self, title):
        self.__title = title

    def getTittle(self):
        return self.__title

    def createState(self):
        return EditorState(self.__content, self.__title)

    def restore(self, state):
        self.__content = state.content
        self.__title = state.title

    def __str__(self):
        return f"Title: {self.__title}. Content: {self.__content}"