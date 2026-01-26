from src.repositories.sqlite_repository import SQLiteTripRepository
from src.repositories.trip_repository import TripRepository
from src.business_logic.trip_servis import TripServis

def build_trip_service() -> TripServis:
    repo = SQLiteTripRepository("src/data/trips.db")
    return TripServis(repo)