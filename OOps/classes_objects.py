class Student:

    def __init__(self,name:str,age:int,gender:str) -> None:
        print("This is a constructor method")
        self.name = name
        self.age = age
        self.gender = gender

    def dispaly(self) -> None:
        print(f"My name is {self.name} and my age is {self.age} and my gender is {self.gender} ")

    def get_age(self) -> int:
        return self.age
s1 = Student("Alice", 20, "Female")
s1.dispaly()
print(s1.get_age())
