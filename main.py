from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from trip_repository import TripRepository
from trip_servis import TripServis
from trip_model import Trip
            

trip_repo = TripRepository()
trip_servis = TripServis(trip_repo)
trip1_data = Trip(2, "Kiyv", "Lviv", "10:00", 15, 1, 500.0, "Петро")
trip2_data = Trip(99, "Odessa", "Harkiv", "12:00", 30, 5, 800.0, "Іван")
trip3_data = Trip(7, "Odessa", "Kiyv", "14:00", 20, 0, 600.0, "Сидор")

trip_servis.create_trip(trip1_data)
trip_servis.create_trip(trip2_data)
trip_servis.create_trip(trip3_data)

trip_servis.book_a_seat(2, 4)
print(trip_servis.get_trip(2))
trip_servis.calcel_book(2, 2)
print(trip_servis.get_trip(2))
trip_servis.stat()
trip_servis.search_trip(None, " Harkiv")




app = FastAPI()
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
    if type(result) is list:
        trips_data = [trip.__dict__ for trip in result]
        return JSONResponse(trips_data, status_code=200)   
    else:
        for key, value in result.items():
            return JSONResponse({key: value}, status_code=200)
    return JSONResponse({"error": "No trips found"}, status_code=404)