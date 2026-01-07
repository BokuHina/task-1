from abc import ABC, abstractmethod
import sqlite3
from typing import List, Optional
from trip_model import AddTrip, Trip

class TripRepositoryAbc(ABC):
  

    @abstractmethod
    def add(self, trip: AddTrip) -> None:
        pass

    @abstractmethod
    def get_by_id(self, trip_id: int) -> Optional[Trip]:
        pass

    @abstractmethod
    def list(self) -> List[Trip]:
        pass

    @abstractmethod
    def update(self, trip: Trip) -> None:
        pass


class SQLiteTripRepository(TripRepositoryAbc):
    
    def __init__(self, db_path):
        self.db_path = db_path
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='trips'")
        result = cursor.fetchone() # Получаем первую (и единственную) строку результата
        print("Result of table check:", result)
        create_table_query = """
            CREATE TABLE IF NOT EXISTS trips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_city TEXT NOT NULL,
            to_city TEXT NOT NULL,
            departure_time TEXT NOT NULL,
            seats_total INTEGER NOT NULL,
            seats_taken INTEGER DEFAULT 0,
            price REAL NOT NULL,
            driver_name TEXT
        );
        """
        cursor.execute(create_table_query)

        connection.commit()
        connection.close()



    def add(self, trip: AddTrip) -> None:
        add_tpi_query = """
            INSERT INTO trips (from_city, to_city, departure_time, seats_total, price, driver_name)
            VALUES (?, ?, ?, ?, ?, ?);
        """   
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(add_tpi_query, (trip.from_city, trip.to_city, trip.departure_time, trip.seats_total, trip.price, trip.driver_name))
        connection.commit()
        connection.close()

       
    def get_by_id(self, trip_id: int) -> Optional[Trip]:
        get_by_id_query = """
            SELECT id, from_city, to_city, departure_time, seats_total, seats_taken, price, driver_name
            FROM trips
            WHERE id = ?;  
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(get_by_id_query, (trip_id,))
        result = cursor.fetchone()

        if result:
            return Trip(
                id=result[0],
                from_city=result[1],
                to_city=result[2],
                departure_time=result[3],
                seats_total=result[4],
                seats_taken=result[5],
                price=result[6],
                driver_name=result[7]
            )
        return None

    def list(self) -> List[Trip]:
        list_query = """
            SELECT *
            FROM trips;
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(list_query)
        results = cursor.fetchall()
        connection.close()

        trips = []
        for result in results:
            trip = Trip(
                id=result[0],
                from_city=result[1],
                to_city=result[2],
                departure_time=result[3],
                seats_total=result[4],
                seats_taken=result[5],
                price=result[6],
                driver_name=result[7]
            )
            trips.append(trip)
        return trips

    def update(self, trip: Trip) -> Trip:
        update_query = """
            UPDATE trips
            SET from_city = ?, to_city = ?, departure_time = ?, seats_total = ?, seats_taken = ?, price = ?, driver_name = ?
            WHERE id = ?;
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(update_query, (trip.from_city, trip.to_city, trip.departure_time, trip.seats_total, trip.seats_taken, trip.price, trip.driver_name, trip.id))
        connection.commit()
        connection.close()
        return self.get_by_id(trip.id)

  