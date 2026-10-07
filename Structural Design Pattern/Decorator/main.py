from coffee import Coffee
from addons import Milk,Sugar,Cream


coffee = Coffee()
coffee = Milk(coffee)
print(coffee.get_cost(),coffee.get_desc())

coffee1 = Coffee()
coffee1 = Sugar(coffee1)
coffee1 = Cream(coffee1)
print(coffee1.get_cost(),coffee1.get_desc())
