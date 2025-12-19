from trip_repository import TripRepository
from add_trips import AddTrip
from trip_model import Trip

class TripServis:
    def __init__(self, trip_repository):
        self.trip_repository = trip_repository
        self._id_counter = 1

    def create_trip(self, data: AddTrip) -> Trip:
        trip = Trip(
            id=self._id_counter,
            from_city=data.from_city,
            to_city=data.to_city,
            departure_time=data.departure_time,
            seats_total=data.seats_total,
            seats_taken=0,
            price=data.price,
            driver_name=data.driver_name
        )

        self.trip_repository.add(trip)
        self._id_counter += 1
        return trip

# додала ще одну функцію для отримання просто за id поїздку
    def get_trip(self, trip_id, from_city = None, to_city = None):
        return self.trip_repository.get_by_id(trip_id)

    def search_trip(self, from_city = None, to_city = None):
        trip_list = self.trip_repository.get_all()
        filtered = []
        if from_city is not None and to_city is not None:
            for trip in trip_list:
                if trip.from_city == from_city and trip.to_city == to_city:
                    filtered.append(trip)
        elif from_city is not None :
            for trip in trip_list:
                if trip.from_city == from_city :
                    filtered.append(trip)
        elif to_city is not None:
            for trip in trip_list:
                if trip.to_city == to_city:
                    filtered.append(trip)
        else:
            return trip_list
        return filtered

    def book_a_seat(self, trip_id, seats):
        trip = self.trip_repository.get_by_id(trip_id)
        if trip is None:
            raise ValueError
        if (trip.seats_taken + seats) > trip.seats_total or trip.seats_taken == trip.seats_total:
            raise ValueError
        trip.seats_taken += seats
        self.trip_repository.update(trip)

    def calcel_book(self, trip_id, seats):
        trip = self.trip_repository.get_by_id(trip_id)
        if trip is None:
            raise ValueError
        if (trip.seats_taken - seats) < 0 or (trip.seats_taken - seats) == 0:
            raise ValueError
        trip.seats_taken -= seats
        self.trip_repository.update(trip)

    def stat(self): # метод для показу статистики
        trip_list = self.trip_repository.get_all()
        count, seats = 0, 0 
        for trip in trip_list:
            seats += trip.seats_total - trip.seats_taken
            count += 1
        return count, seats
    