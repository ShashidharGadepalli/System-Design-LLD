from BehavioralDesignPattern.State.tranport_mode import TransportMode

class Walk(TransportMode):

    def ETA(self):
        print(" Walking will take 45 mins")

    def directions(self):
        print("Kepp walking on the footpath along denton flyover and turn right on Tacobell")