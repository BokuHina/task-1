from domain.sqlite_repository import SQLiteTripRepository
from trip_model import Trip, AddTrip

class TripServis:
    def __init__(self, sqlite_repository):
        self.sqlite_repository = sqlite_repository

    def create_trip(self, data: AddTrip) -> Trip:
        self.sqlite_repository.add(data)

# додала ще одну функцію для отримання просто за id поїздку
    def get_trip(self, trip_id: int) -> Trip | None:
        return self.sqlite_repository.get_by_id(trip_id)

    def search_trip(self, from_city = None, to_city = None):
        trip_list = self.sqlite_repository.list()
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
        trip = self.sqlite_repository.get_by_id(trip_id)
        if trip is None:
            raise ValueError
        if (trip.seats_taken + seats) > trip.seats_total or trip.seats_taken == trip.seats_total:
            raise ValueError
        trip.seats_taken += seats
        self.sqlite_repository.update(trip)

    def calcel_book(self, trip_id, seats):
        trip = self.sqlite_repository.get_by_id(trip_id)
        if trip is None:
            raise ValueError
        if (trip.seats_taken - seats) < 0 or (trip.seats_taken - seats) == 0:
            raise ValueError
        trip.seats_taken -= seats
        self.sqlite_repository.update(trip)

    def stat(self): # метод для показу статистики
        trip_list = self.sqlite_repository.list()
        count, seats = 0, 0 
        for trip in trip_list:
            seats += trip.seats_total - trip.seats_taken
            count += 1
        return count, seats
    