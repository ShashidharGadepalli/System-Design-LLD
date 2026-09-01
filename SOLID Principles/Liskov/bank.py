from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def __init__(self, balance: int) -> None:
        self.balance = balance

    @abstractmethod
    def deposit(self) -> None:
        pass

