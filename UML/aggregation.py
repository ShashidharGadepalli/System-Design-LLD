# Student class can exist Independently
class Student:

    def __init__(self,name :str, roll_no:int) -> None:
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self) -> str:
        return self.__name

    def get_roll_no(self) -> int:
        return self.__roll_no

# Department clsss contains student- Aggregation

class Department:

    def __init__(self, dept_name:str) -> None:
        self.__dept_name = dept_name
        self.__students = []

    def add_student(self, student: Student) -> None:
        self.__students.append(student)

    def show_students(self) -> None:
        print(f"Students in {self.__dept_name} Department:")
        for student in self.__students:
            print(f"Name: {student.get_name()}, Roll No: {student.get_roll_no()}")

s1 = Student("Alice", 101)
s2 = Student("Bob", 102)
s3 = Student("Charlie", 103)
cs_dept = Department("Computer Science")

cs_dept.add_student(s1)
cs_dept.add_student(s2)
cs_dept.add_student(s3)

cs_dept.show_students()


del cs_dept

print(f"Student {s1.get_name()} still exists after deleting the department.")