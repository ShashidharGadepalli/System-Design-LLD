from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass

class UPIPayment(PaymentMethod):
    def pay(self, amount: int) -> None:
        print(f"Processing UPI payment of {amount}.")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: int) -> None:
        print(f"Processing credit card payment of {amount}.")

class PayPalPayment(PaymentMethod):
    def pay(self, amount: int) -> None:
        print(f"Processing PayPal payment of {amount}.")
        