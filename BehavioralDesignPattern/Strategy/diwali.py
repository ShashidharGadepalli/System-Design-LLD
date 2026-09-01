from BehavioralDesignPattern.Strategy.discountstrategy import DiscountStrategy

class Diwali(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        print("Applying Diwali discount...")
        return amount * 0.2  # 20% discount
