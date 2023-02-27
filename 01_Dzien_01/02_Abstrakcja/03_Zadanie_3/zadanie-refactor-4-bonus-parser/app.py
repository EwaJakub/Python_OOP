import sys
import argparse

from googlebooks import GoogleBooksAPI
from inventory import Inventory
from stickerprinter import StickerPrinter


google_books_api = GoogleBooksAPI()
inventory = Inventory('books.json')
stickerprinter = StickerPrinter()

parser = argparse.ArgumentParser(description='Asystent księgarza')
parser.add_argument(
    'command',
    metavar='COMMAND',
    type=str,
    choices=['import', 'add', 'remove', 'print-price-sticker'],
    help='Akcja do wykonania: import / add / remove / print-price-sticker'
)
parser.add_argument('--isbn', type=str, help='Numer ISBN książki')
parser.add_argument('--amount', type=int, help='Liczba książek do dodania/usunięcia')
parser.add_argument('--price', type=float, help='Cena importowanej książki')


def import_book(isbn, price):
    book_info = google_books_api.get_book(isbn)
    if book_info:
        inventory.add_new_book(isbn, book_info['title'], book_info['authors'], price)
    else:
        print('Nie znaleziono książki w Google Books')


def add_books(isbn, amount):
    success = inventory.add_books(isbn, amount)
    if not success:
        print('Nie znaleziono książki w magazynie')


def remove_books(isbn, amount):
    success = inventory.remove_books(isbn, amount)
    if not success:
        print('Nie znaleziono książki w magazynie')


def print_price_sticker(isbn):
    book_info = inventory.get_book_info(isbn)
    if book_info:
        stickerprinter.print_price_sticker(isbn, book_info['title'], book_info['price'])
    else:
        print('Nie znaleziono książki w magazynie')


def main():
    args = parser.parse_args()

    if args.command == 'import':
        if args.isbn is None:
            print('Musisz podać numer ISBN importowanej książki')
        elif args.price is None:
            print('Musisz podać cenę importowanej książki')
        else:
            import_book(args.isbn, args.price)

    elif args.command == 'add':
        if args.isbn is None:
            print('Musisz podać numer ISBN książki, której stan magazynowy zmieniasz')
        elif args.amount is None:
            print('Musisz podać ile sztuk książki chcesz dodać')
        else:
            add_books(args.isbn, args.amount)

    elif args.command == 'remove':
        if args.isbn is None:
            print('Musisz podać numer ISBN książki, której stan magazynowy zmieniasz')
        elif args.amount is None:
            print('Musisz podać ile sztuk książki chcesz usunąć')
        else:
            remove_books(args.isbn, args.amount)

    elif args.command == 'print-price-sticker':
        if args.isbn is None:
            print('Musisz podać numer ISBN książki, dla której chcesz wydrukować naklejkę z ceną')
        else:
            print_price_sticker(args.isbn)


if __name__ == '__main__':
    main()
