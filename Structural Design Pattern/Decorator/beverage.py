from abc import ABC, abstractmethod

class Bevearage(ABC):

    @abstractmethod
    def get_desc(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass
