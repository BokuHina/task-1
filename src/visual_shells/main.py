from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.business_logic.trip_servis import TripServis
from src.domain_model.trip_model import AddTrip
from src.assembly_place.conteiner import build_trip_service


trip_servis = build_trip_service()

# trip_repo.type()
app = FastAPI()

# trip1_data = AddTrip("Kiyv", "Lviv", "10:00", 15, 500.0, "Petro")
# trip2_data = AddTrip("Odessa", "Harkiv", "12:00", 30, 800.0, "Sergiy")
# trip3_data = AddTrip("Odessa", "Kiyv", "14:00", 20, 600.0, "Sidor")
# trip4_data = AddTrip("Lviv", "Kiyv", "16:00", 10, 550.0, "Mariya")
# trip5_data = AddTrip("Harkiv", "Odessa", "18:00", 25, 750.0, "Olena")
# trip6_data = AddTrip("Lviv", "Odessa", "20:00", 18, 700.0, "Andriy")
# trip7_data = AddTrip("Kiyv", "Harkiv", "22:00", 12, 650.0, "Viktor")
# trip8_data = AddTrip("Harkiv", "Lviv", "09:00", 22, 720.0, "Svitlana")

# trip_servis.create_trip(trip1_data)
# trip_servis.create_trip(trip2_data)
# trip_servis.create_trip(trip3_data)
# trip_servis.create_trip(trip4_data)
# trip_servis.create_trip(trip5_data)
# trip_servis.create_trip(trip6_data)
# trip_servis.create_trip(trip7_data)
# trip_servis.create_trip(trip8_data)

# trip_servis.book_a_seat(2, 4)

@app.get('/')

def read_root():
    return {"Hello": "World"}

@app.get('/helth')

def helth():
    return JSONResponse({'status':'ok'}, status_code=200)

@app.get('/trips')
async def trips (from_city: str|None = None, to_city: str|None = None):
    result = trip_servis.search_trip(from_city, to_city)
    trips_data = [trip.__dict__ for trip in result]
    return JSONResponse(trips_data, status_code=200)

