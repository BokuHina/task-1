from trip_repository import TripRepository
from trip_servis import TripServis
from trip_model import Trip
            

trip_repo = TripRepository()
trip_servis = TripServis(trip_repo)

trip1_data = Trip(1, "Київ", "Львів", "10:00", 5, 1, 500.0, "Петро")
trip2_data = Trip(2, "Одеса", "Харків", "12:30", 30, 0, 800.0, "Іван")
trip3_data = Trip(3, "Запоріжжя", "Львів", "21:45", 6, 3, 1050.0, "Владислав")

trip_servis.create_trip(trip1_data)

#перевірка пошуку поїздок з існуючим id та з неіснуючим
assert trip_servis.get_trip(1) != None, "Поїздку не було додано"
assert trip_servis.get_trip(99) == None, "Поїздка не повинна інсувати" 

trip_servis.create_trip(trip2_data)
trip_servis.create_trip(trip3_data)

# перевірка на бронювання 
trip_servis.book_a_seat(2, 4)
trip2 = trip_servis.get_trip(2)
assert trip2.seats_taken ==4, "Місце не було заброньовано"
print(trip2)

#перевірка на зняття бронювання 
trip_servis.calcel_book(2, 2)
assert trip2.seats_taken != 4, "Місце не було повернуто"

print(trip_servis.stat())

# перевірка пошуку за фільтрами
result = trip_servis.search_trip(None, "Львів")
assert len(result) > 0, "Пошук не повернув жодної поїздки"

assert all(trip.to_city == "Львів" for trip in result), "Знайдено поїздку не в Львів"
