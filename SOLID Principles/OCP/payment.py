from paymentmethod import PaymentMethod
from paymentmethod import UPIPayment, CreditCardPayment, PayPalPayment

class Payment:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: int) -> None:
        self.payment_method.pay(amount)

payment_method = UPIPayment()
payment = Payment(payment_method)
payment.process_payment(1000)

payment_method = CreditCardPayment()
payment = Payment(payment_method)
payment.process_payment(2000)   