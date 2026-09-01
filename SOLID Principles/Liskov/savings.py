from withdraw import Withdarwable

class SavingsAccount(Withdarwable):
    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")