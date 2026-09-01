from bank import Bank

class FixedAccount(Bank):

    def __init__(self, balance: int) -> None:
        super().__init__(balance)

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposited {amount} in Fixed Deposit. New balance is {self.balance}.")