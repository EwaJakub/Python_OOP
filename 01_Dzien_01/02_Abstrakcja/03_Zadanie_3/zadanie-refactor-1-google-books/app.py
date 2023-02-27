import sys
import json
import webbrowser
import tempfile
import os
import textwrap

from googlebooks import GoogleBooksAPI


google_books_api = GoogleBooksAPI()


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
        with open('books.json', 'r') as f:
            store_content = json.loads(f.read())
            store_content[isbn] = {
                'title': book_info['title'],
                'authors': book_info['authors'],
                'amount': 0,
                'price': price,
            }
        with open('books.json', 'w') as f:
            f.write(json.dumps(store_content))
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
    with open('books.json', 'r') as f:
        store_content = json.loads(f.read())
    if isbn not in store_content:
        print('Nie znaleziono książki w magazynie')
        sys.exit()
    store_content[isbn]['amount'] += to_add
    with open('books.json', 'w') as f:
        f.write(json.dumps(store_content))

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
    with open('books.json', 'r') as f:
        store_content = json.loads(f.read())
    if isbn not in store_content:
        print('Nie znaleziono książki w magazynie')
        sys.exit()
    store_content[isbn]['amount'] -= to_remove
    with open('books.json', 'w') as f:
        f.write(json.dumps(store_content))

if sys.argv[1] == 'print-price-sticker':
    if len(sys.argv) <= 2:
        print('Musisz podać numer ISBN książki, dla której chcesz wydrukować naklejkę z ceną')
        sys.exit()
    else:
        isbn = sys.argv[2]
    with open('books.json') as f:
        store_content = json.loads(f.read())
    if isbn not in store_content:
        print('Nie znaleziono książki w magazynie')
        sys.exit()
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as price_sticker_file:
        price_sticker_file.write(textwrap.dedent(f'''
            <!DOCTYPE html>
            <html>
            <head>
            <link href='https://fonts.googleapis.com/css?family=Libre Barcode 39' rel='stylesheet'>
            </head>
            <body>
            <div style="float:left; border: 1px dotted black; padding: 10px; text-align: center">
            <p>{store_content[isbn]['title']} - {store_content[isbn]['price']}zł</p>
            <p style="font-family: 'Libre Barcode 39'; font-size: 22px;">{isbn} {store_content[isbn]['price']}</p>
            </div>
            <script type="text/javascript">window.print(); window.close();</script>
            </body>
            </html>
        '''))
        webbrowser.open(os.path.realpath(price_sticker_file.name))
