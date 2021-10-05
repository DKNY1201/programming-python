class History:
    def __init__(self):
        self.__states = []

    def push(self, state):
        self.__states.append(state)

    def pop(self):
        if self.__states:
            return self.__states.pop()