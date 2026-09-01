from abc import ABC, abstractmethod
from bank import Bank

class Withdarwable(Bank):

    def __init__(self, balance: int) -> None:
        super().__init__(balance)
        
    @abstractmethod
    def withdraw(self,amount) -> None:
        pass

