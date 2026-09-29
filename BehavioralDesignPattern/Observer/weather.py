from observer import Observer

class Weather:

    def __init__(self):
        self._observers = []
        self._temperature = None

    def add_observer(self, observer:Observer):
        self._observers.append(observer)

    def remove_observer(self, observer:Observer):
        self._observers.remove(observer)

    def update_temperature(self, temp):
        self._temperature = temp
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)