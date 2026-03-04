from abc import ABC, abstractmethod
class Readable(ABC):
    @abstractmethod
    def read(self):
        pass