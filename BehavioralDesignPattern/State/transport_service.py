from BehavioralDesignPattern.State.tranport_mode import TransportMode
class TransportService:

    def __init__(self, transport_mode:TransportMode):
        self._transport_mode = transport_mode

    def set_mode(self,new_mode: TransportMode):
        self._transport_mode = new_mode

    def eta(self):
        return self._transport_mode.ETA()

    def directions(self):
        return self._transport_mode.directions()