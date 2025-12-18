from dataclasses import dataclass
@dataclass 
class Trip:
    id: int
    from_city: str
    to_city: str
    departure_time: str
    seats_total: int
    seats_taken: int
    price: float
    driver_name: str

# обробка не правильного задання параметрів для поїздки
    def __post_init__ (self):
        if self.seats_total <=0:
            raise ValueError
        if self.seats_taken > self.seats_total or self.seats_taken < 0:    #додала ще одну перевірку для seats_taken
            raise ValueError
        if self.price <=0:
            raise ValueError