from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from trip_model import Trip
# абстрактний клас-сховище

class TripRepositoryAbc(ABC):

    @abstractmethod
    def add(self, trip:Trip) -> None:
        pass

    @abstractmethod
    def get_by_id(self, trip_id: int) -> Optional[Trip]:
        pass

    @abstractmethod
    def get_all(self) -> List[Trip]:
        pass

    @abstractmethod
    def update(self, trip:Trip) -> None:
        pass


class TripRepository(TripRepositoryAbc):
    def __init__(self):
        self._trips: Dict[int, Trip] = {}

    def add(self, trip: Trip) -> None:
        if trip.id in self._trips:
            raise ValueError(f"Trip with id {trip.id} already exists")

        self._trips[trip.id] = trip

    def get_by_id(self, trip_id: int) -> Optional[Trip]:
        return self._trips.get(trip_id)

    def get_all(self) -> List[Trip]:
        return list(self._trips.values())

    def update(self, trip: Trip) -> None:
        if trip.id not in self._trips:
            raise ValueError(f"Trip with id {trip.id} not found")
        self._trips[trip.id] = trip