from observer import Observer

class TVDisplay(Observer):
    def update(self, temp):
        print(f"TV Display: Temperature updated to {temp} degrees.")