class Teacher:

    def __init__(self, name:str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def teach(self, student: 'Students') -> None:
        print(f"{self.__name} is teaching {student.get_name()}")

class Students:
    
    def __init__(self, name:str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

teacher = Teacher("Mr. Smith")
student = Students("John Doe")
teacher.teach(student)