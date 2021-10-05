from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def draw(self):
        pass