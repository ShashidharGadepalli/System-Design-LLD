from abc import ABC, abstractmethod

class Workable(ABC):

    @abstractmethod
    def work(self) -> None:
        pass

class Eatable(ABC):

    @abstractmethod
    def eat(self) -> None:
        pass

class Robot(Workable):

    def work(self) -> None:
        print("Robot is working.")

class Employee(Workable, Eatable):

    def work(self) -> None:
        print("Employee is working.")

    def eat(self) -> None:
        print("Employee is eating.")

r = Robot()
r.work()  # Output: Robot is working.
E = Employee()
E.work()  # Output: Employee is working.
E.eat()  # Output: Employee is eating.