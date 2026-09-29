from BehavioralDesignPattern.State.tranport_mode import TransportMode
from BehavioralDesignPattern.State.transport_service import TransportService
from BehavioralDesignPattern.State.bike import Bike
from BehavioralDesignPattern.State.walk_mode import Walk

transport_service = TransportService(Bike())
transport_service.eta()
transport_service.directions()

transport_service.set_mode(Walk())
transport_service.eta()
transport_service.directions()