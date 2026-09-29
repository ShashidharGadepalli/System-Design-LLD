from BehavioralDesignPattern.State.tranport_mode import TransportMode

class Bike(TransportMode):

    def ETA(self):
        print("Bike will Take 20 mins ")

    def directions(self):
        print("Take the Denton flyover and slide right on exit 27")