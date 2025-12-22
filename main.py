from fastapi import FastAPI
from fastapi.responses import JSONResponse
from add_trips import AddTrip
from trip_repository import TripRepository
from trip_servis import TripServis

trip_repo = TripRepository()
trip_servis = TripServis(trip_repo)

app = FastAPI()

trip1_data = AddTrip("Kiyv", "Lviv", "10:00", 15, 500.0, "Петро")
trip2_data = AddTrip("Odessa", "Harkiv", "12:00", 30, 800.0, "Іван")
trip3_data = AddTrip("Odessa", "Kiyv", "14:00", 20, 600.0, "Сидор")
trip4_data = AddTrip("Lviv", "Kiyv", "16:00", 10, 550.0, "Марія")
trip5_data = AddTrip("Harkiv", "Odessa", "18:00", 25, 750.0, "Олена")
trip6_data = AddTrip("Lviv", "Odessa", "20:00", 18, 700.0, "Андрій")
trip7_data = AddTrip("Kiyv", "Harkiv", "22:00", 12, 650.0, "Віктор")
trip8_data = AddTrip("Harkiv", "Lviv", "09:00", 22, 720.0, "Світлана")

trip_servis.create_trip(trip1_data)
trip_servis.create_trip(trip2_data)
trip_servis.create_trip(trip3_data)
trip_servis.create_trip(trip4_data)
trip_servis.create_trip(trip5_data)
trip_servis.create_trip(trip6_data)
trip_servis.create_trip(trip7_data)
trip_servis.create_trip(trip8_data)

@app.get('/')

def read_root():
    return {"Hello": "World"}

@app.get('/helth')

def helth():
    return JSONResponse({'status':'ok'}, status_code=200)

@app.get('/trips')
async def trips (from_city: str|None = None, to_city: str|None = None):
    if from_city and to_city:
        result = trip_servis.search_trip(from_city, to_city)
        
    elif from_city:
        result = trip_servis.search_trip(from_city, None)
       
    elif to_city:
        result = trip_servis.search_trip(None, to_city)
        
    else:
        result = trip_servis.search_trip()
    
    trips_data = [trip.__dict__ for trip in result]
    return JSONResponse(trips_data, status_code=200)
