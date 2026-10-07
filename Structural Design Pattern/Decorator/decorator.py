from beverage import Bevearage
from coffee import Coffee

class Decorator(Bevearage):

    def __init__(self,coffee:Coffee):
        self._coffee = coffee

    def get_desc(self):
        return self._coffee.get_desc()

    def get_cost(self):
        return self._coffee.get_cost()
