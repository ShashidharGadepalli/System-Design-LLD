from abc import ABC, abstractmethod

class TransportMode(ABC):

    @abstractmethod
    def ETA(self):
        pass

    @abstractmethod
    def directions(self):
        pass