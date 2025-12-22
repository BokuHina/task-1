from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from trip_model import AddTrip, Trip
# абстрактний клас-сховище

class TripRepositoryAbc(ABC):

    @abstractmethod
    def add(self, trip: AddTrip) -> None:
        pass

    @abstractmethod
    def get_by_id(self, trip_id: int) -> Optional[Trip]:
        pass

    @abstractmethod
    def get_all(self) -> List[Trip]:
        pass

    @abstractmethod
    def update(self, trip: Trip) -> None:
        pass

    @abstractmethod
    def get_next_id(self) -> int:
        pass


class TripRepository(TripRepositoryAbc):
    def __init__(self):
        self._trips: Dict[int, Trip] = {}

    def add(self, trip: AddTrip) -> None:
        id = self.get_next_id()
        _trip = Trip(
            id=id,
            from_city=trip.from_city,
            to_city=trip.to_city,
            departure_time=trip.departure_time,
            seats_total=trip.seats_total,
            seats_taken=0,
            price=trip.price,
            driver_name=trip.driver_name
        )
        if id in self._trips:
            raise ValueError(f"Trip with id {id} already exists")
        self._trips[_trip.id] = _trip

    def get_by_id(self, trip_id: int) -> Optional[Trip]:
        return self._trips.get(trip_id)

    def get_all(self) -> List[Trip]:
        return list(self._trips.values())

    def update(self, trip: Trip) -> None:
        if trip.id not in self._trips:
            raise ValueError(f"Trip with id {trip.id} not found")
        self._trips[trip.id] = trip

    def get_next_id(self) -> int:
        if not self._trips:
            return 1
        return max(self._trips.keys()) + 1