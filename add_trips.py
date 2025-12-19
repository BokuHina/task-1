from dataclasses import dataclass

from dataclasses import dataclass

@dataclass
class AddTrip:
    from_city: str
    to_city: str
    departure_time: str
    seats_total: int
    price: float
    driver_name: str

        