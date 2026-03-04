from abc import ABC,abstractmethod

class Writable(ABC):
    @abstractmethod
    def write(self, data):
        pass
    