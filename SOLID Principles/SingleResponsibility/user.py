class User:

    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self)->None:
        print(f"My Name is {self.name}, I am {self.age} years old.")

    def is_adult(self) -> bool:
        return self.age > 18
