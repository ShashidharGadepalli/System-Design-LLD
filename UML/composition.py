class Engine:
    def __init__(self, enginer_type, horsepower) -> None:
        self.__enginer_type = enginer_type
        self.__horsepower = horsepower

    def get_details(self) -> str:
        return f"Engine Type: {self.__enginer_type}, Horsepower: {self.__horsepower}"

    def start(self) -> None:
        print(f"{self.__enginer_type} engine started")


# car class owns engine - Composition
class Car:

    def __init__(self, brand,model, enfine_type, horsepower) -> None:
        self.__brand = brand
        self.__model = model

        # engine is created within the Car class, indicating a composition relationship
        self.__engine = Engine(enfine_type, horsepower)

    def get_car_details(self) -> None:

        print(f"car brand : {self.__brand}, model: {self.__model}")
        print(self.__engine.get_details())

    def start_car(self) -> None:
        print(f"Starting the {self.__brand} {self.__model}")
        self.__engine.start()


my_car = Car("Toyota", "Camry", "V6", 301)
my_car.get_car_details()
my_car.start_car()

print("\n destroying the car")
del my_car

