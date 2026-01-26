from src.business_logic.trip_servis import TripServis
from src.domain_model.trip_model import AddTrip
from src.assembly_place.conteiner import build_trip_service

service = build_trip_service()

# перевірка чи створюється бд і таблиця
print(service.search_trip())
# перевірка чи зберігається поїздка з попередьої сесії
assert service.get_trip(1) != None, "Поїздку не було додано"



# # первірка сервісних методів
# new_trip = AddTrip("TestCityA", "TestCityB", "15:30", 20, 450.0, "TestDriver")
# service.create_trip(new_trip)
# print(service.search_trip("TestCityA", "TestCityB"))

service.book_a_seat(9, 10)
print(service.search_trip("TestCityA", "TestCityB"))
service.calcel_book(9, 5)
print(service.search_trip("TestCityA", "TestCityB"))
count, seats = service.stat()
print(f"Total trips: {count}, Total available seats: {seats}")