
class Animal:

    def __init__(self, name: str,age: int) -> None:
        self.name = name
        self.age = age
        print("This is a constructor method of Animal class")

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

    def move(self):
        print("Animal is moving")

class Dog(Animal):

    def __init__(self, name: str, age: int, breed: str) -> None:
        
        super().__init__(name, age)
        self.breed = breed
        print("This is a constructor method of Dog class")

    def bark(self):
        print("I am barking")

    def display_info(self):
        print(f"My name is {self.name} and my age is {self.age}")

    def move(self):
        print("Dog is running on all fours")

dog = Dog("Buddy", 3, "Golden Retriever")
dog.display_info()
dog.move()
