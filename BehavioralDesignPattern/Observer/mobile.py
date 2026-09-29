from observer import Observer

class MobileDisplay(Observer):
    def update(self, temp):
        print(f"Mobile Display: Temperature updated to {temp} degrees.")