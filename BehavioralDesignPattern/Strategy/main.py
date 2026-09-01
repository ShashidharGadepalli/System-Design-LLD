from BehavioralDesignPattern.Strategy.discountservice import DiscountService
from BehavioralDesignPattern.Strategy.firstorder import FirstOrder
from BehavioralDesignPattern.Strategy.diwali import Diwali

diwali_strategy = Diwali()
first_order_strategy = FirstOrder()
discount_service = DiscountService(first_order_strategy)
answer = discount_service.process_discount(100.0)
print(answer)



discount_service.set_strategy(diwali_strategy)
answer = discount_service.process_discount(100.0)
print(answer) 