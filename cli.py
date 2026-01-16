import argparse
from sqlite_repository import SQLiteTripRepository
from trip_servis import TripServis
from trip_model import AddTrip, Trip


repo = SQLiteTripRepository("data/trips.db")
service = TripServis(repo)

parser = argparse.ArgumentParser(description="A simple CLI tool example.")

subparsers = parser.add_subparsers(dest="command", help="доступні команди")

parser_add = subparsers.add_parser('add', help='Додає новий елемент')
parser_add.add_argument('-n', '--name', type=str, help='Ім\'я елемента для додавання')
parser_add.add_argument('-from', '--from_city', type=str, help='Місто відправлення')
parser_add.add_argument('-to', '--to_city', type=str, help='Місто призначення')
parser_add.add_argument('-dt', '--departure_time', type=str, help='Час відправлення')
parser_add.add_argument('-st', '--seats_total', type=int, help='Загальна кількість місць')
parser_add.add_argument('-p', '--price', type=float, help='Ціна поїздки')
parser_add.add_argument('-dn', '--driver_name', type=str, help='Ім\'я водія')

# Парсер для команди 'list-trips'
parser_list = subparsers.add_parser('list-trips', help='Показує список елементів')

# парсер для команди 'search-trip'
parser_search = subparsers.add_parser('search-trip', help='Шукає елементи за місцевем відправлення та призначення')
parser_search.add_argument('--from_city', type=str, default=None, help='Звідки відправляється поїздка')
parser_search.add_argument('--to_city', type=str, default=None, help='Куди відправляється поїздка')

# Парсер для команди 'stat'
parser_stat = subparsers.add_parser('stat', help='Показує статистику елементів')

#  'book-seat'
parser_book = subparsers.add_parser('book-seat', help='Бронює місце в поїздці')
parser_book.add_argument('trip_id', type=int, help='ID поїздки для бронювання місця')

#  'cancel-book'
parser_cancel = subparsers.add_parser('cancel-book', help='Скасовує бронювання місця в поїздці')
parser_cancel.add_argument('trip_id', type=int, help='ID поїздки для скасування бронювання місця')

# Зчитуємо аргументи
args = parser.parse_args()

# Виконуємо логіку
if args.command == 'add':
    trip = AddTrip(
        from_city=args.from_city,
        to_city=args.to_city,
        departure_time=args.departure_time,
        seats_total=args.seats_total,
        price=args.price,
        driver_name=args.driver_name
    )
    service.create_trip(trip)
elif args.command == 'list-trips':
    print(service.search_trip())
elif args.command == 'search-trip':
    print(service.search_trip(args.from_city, args.to_city))
elif args.command == 'stat':
    print(service.stat())
elif args.command == 'book-seat':
    try:
        service.book_a_seat(args.trip_id, 1)
        print(f"Місце в поїздці з ID {args.trip_id} успішно заброньовано.")
    except ValueError:
        print(f"Не вдалося забронювати місце в поїздці з ID {args.trip_id}.")
elif args.command == 'cancel-book':
    try:
        service.calcel_book(args.trip_id, 1)
        print(f"Бронювання місця в поїздці з ID {args.trip_id} успішно скасовано.")
    except ValueError:
        print(f"Не вдалося скасувати бронювання місця в поїздці з ID {args.trip_id}.")
else:   
    parser.print_help()








# parser_list = subparsers.add_parser("list-trips", help="List all items.")

# def main():
#     args = parser.parse_args()

#     if args.command == "list-trips":
#         trips = service.search_trip()
#         for trip in trips:
#             print(trip)