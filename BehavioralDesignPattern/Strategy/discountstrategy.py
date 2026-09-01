from abc import ABC, abstractmethod

class DiscountStrategy(ABC):

    @abstractmethod
    def calculate_discount(self, amount: float) -> float:
        pass