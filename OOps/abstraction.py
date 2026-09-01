from abc import ABC, abstractmethod

from sympy import shape

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class implementing the abstract methods
class Rectangle(Shape):

    def __init__(self,lenght: int,width:int) -> None:
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    def perimeter(self):
        return 2 * (self.lenght + self.width)

class Circle(Shape):
    
    def __init__(self,radius:int) -> None:
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

r = Rectangle(5, 10)
print(f"Area of rectangle: {r.area()}")