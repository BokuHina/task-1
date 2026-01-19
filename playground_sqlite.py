from sqlite_repository import SQLiteTripRepository
from trip_model import AddTrip
from trip_servis import TripServis

repo = SQLiteTripRepository("data/trips.db")
service = TripServis(repo)

# перевірка чи створюється бд і таблиця
print(service.search_trip())
# перевірка чи зберігається поїздка з попередьої сесії
assert service.get_trip(1) != None, "Поїздку не було додано"



# # первірка сервісних методів
# new_trip = AddTrip("TestCityA", "TestCityB", "15:30", 20, 450.0, "TestDriver")
# service.create_trip(new_trip)
# print(service.search_trip("TestCityA", "TestCityB"))

# service.book_a_seat(9, 10)
# print(service.search_trip("TestCityA", "TestCityB"))
# service.calcel_book(9, 5)
# print(service.search_trip("TestCityA", "TestCityB"))
# count, seats = service.stat()
# print(f"Total trips: {count}, Total available seats: {seats}")