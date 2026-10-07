from decorator import Decorator

class Milk(Decorator):

    def get_desc(self):
        return super().get_desc() + ", Milk"

    def get_cost(self):
        return super().get_cost() + 5

class Sugar(Decorator):

    def get_desc(self):
        return super().get_desc() + ", Sugar"

    def get_cost(self):
        return super().get_cost() + 2

class Cream(Decorator):

    def get_desc(self):
        return super().get_desc() + ", Cream"

    def get_cost(self):
        return super().get_cost() + 5
    