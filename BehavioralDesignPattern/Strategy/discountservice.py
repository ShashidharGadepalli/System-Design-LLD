from BehavioralDesignPattern.Strategy.discountstrategy import DiscountStrategy

class DiscountService:
    def __init__ (self, discount_strategy: DiscountStrategy):
        self.__discount_strategy = discount_strategy

    def set_strategy(self, new_discount_strategy: DiscountStrategy):
        self.__discount_strategy = new_discount_strategy


    def process_discount(self, amount: float):
        return self.__discount_strategy.calculate_discount(amount)