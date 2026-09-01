class Bank:

    def __init__(self, name:str, balance:int) -> None:
        self.name = name
        # Private attribute
        self.__balance = balance
   # Getter and setter for private attribute
    def get_balance(self) -> None:
        print(f"Current balance: {self.__balance}")

    def deposit(self,amount:int) -> None:
        if self.__isserverlive():
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Server is down. Please try again later.")

    def set_balance(self, amount: int) -> None:
        self.__balance = amount

    def __isserverlive(self) -> bool:
        return True

    def withdraw(self,amount:int) -> None:
        if amount> self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

acc = Bank("John Doe", 1000)
acc.deposit(1000)
acc.withdraw(500)
acc.get_balance()
