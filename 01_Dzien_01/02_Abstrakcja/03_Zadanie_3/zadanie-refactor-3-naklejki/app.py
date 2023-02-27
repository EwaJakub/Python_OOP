import sys

from googlebooks import GoogleBooksAPI
from inventory import Inventory
from stickerprinter import StickerPrinter


google_books_api = GoogleBooksAPI()
inventory = Inventory('books.json')
stickerprinter = StickerPrinter()


if len(sys.argv) <= 1:
    print('Musisz podać polecenie')
    sys.exit()


if sys.argv[1] == 'import':
    if len(sys.argv) <= 2:
        print('Musisz podać numer ISBN importowanej książki')
        sys.exit()
    elif len(sys.argv) <= 3:
        print('Musisz podać cenę importowanej książki')
        sys.exit()
    else:
        isbn = sys.argv[2]
        price = float(sys.argv[3])

    book_info = google_books_api.get_book(isbn)
    if book_info:
        inventory.add_new_book(isbn, book_info['title'], book_info['authors'], price)
    else:
        print('Nie znaleziono książki w Google Books')


if sys.argv[1] == 'add':
    if len(sys.argv) <= 2:
        print('Musisz podać numer ISBN książki, której stan magazynowy zmieniasz')
        sys.exit()
    elif len(sys.argv) <= 3:
        print('Musisz podać ile sztuk książki chcesz dodać')
        sys.exit()
    else:
        isbn = sys.argv[2]
        to_add = int(sys.argv[3])

    success = inventory.add_books(isbn, to_add)
    if not success:
        print('Nie znaleziono książki w magazynie')
        sys.exit()

if sys.argv[1] == 'remove':
    if len(sys.argv) <= 2:
        print('Musisz podać numer ISBN książki, której stan magazynowy zmieniasz')
        sys.exit()
    elif len(sys.argv) <= 3:
        print('Musisz podać ile sztuk książki chcesz usunąć')
        sys.exit()
    else:
        isbn = sys.argv[2]
        to_remove = int(sys.argv[3])

    success = inventory.remove_books(isbn, to_remove)
    if not success:
        print('Nie znaleziono książki w magazynie')
        sys.exit()


if sys.argv[1] == 'print-price-sticker':
    if len(sys.argv) <= 2:
        print('Musisz podać numer ISBN książki, dla której chcesz wydrukować naklejkę z ceną')
        sys.exit()
    else:
        isbn = sys.argv[2]

    book_info = inventory.get_book_info(isbn)
    if not book_info:
        print('Nie znaleziono książki w magazynie')
        sys.exit()

    stickerprinter.print_price_sticker(isbn, book_info['title'], book_info['price'])
