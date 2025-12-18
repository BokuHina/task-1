# ОПИС ПО ЗАПУСКУ ПРОЄКТУ
Щоб запустити веб-сервер потрібно прописати в консоль команду після запуску програми:
```bash
uvicorn main:app --reload
```
Щоб зупенити сервер натискаємо **Ctrl+C**

## ПРИКЛАД ВІДОБРАЖЕННЯ ЗАПИТІВ
   /trips?from_city=Kyiv
   ```bash
[
  {
    "id": 2,
    "from_city": "Kiyv",
    "to_city": "Lviv",
    "departure_time": "10:00",
    "seats_total": 15,
    "seats_taken": 2,
    "price": 500,
    "driver_name": "Петро"
  }
]
```
/trips
 ```bash
[
  {
    "id": 2,
    "from_city": "Kiyv",
    "to_city": "Lviv",
    "departure_time": "10:00",
    "seats_total": 15,
    "seats_taken": 2,
    "price": 500,
    "driver_name": "Петро"
  },
  {
    "id": 99,
    "from_city": "Odessa",
    "to_city": "Harkiv",
    "departure_time": "12:00",
    "seats_total": 30,
    "seats_taken": 0,
    "price": 800,
    "driver_name": "Іван"
  },
  {
    "id": 7,
    "from_city": "Odessa",
    "to_city": "Kiyv",
    "departure_time": "14:00",
    "seats_total": 20,
    "seats_taken": 0,
    "price": 600,
    "driver_name": "Сидор"
  }
]
```
