from BehavioralDesignPattern.Strategy.discountstrategy import DiscountStrategy

class FirstOrder(DiscountStrategy):
    def calculate_discount(self, amount: float) -> float:
        print("Applying first order discount...")
        return amount * 0.1  # 10% discount