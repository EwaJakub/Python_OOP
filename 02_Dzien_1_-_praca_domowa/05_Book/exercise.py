class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        if self.check_isbn(isbn) is True:
            self.isbn = isbn
        else:
            raise ValueError('Błędny kod!')

    @staticmethod
    def check_isbn(isbn):
        corrected_isbn = isbn.replace('-', '')
        try:
            if len(corrected_isbn) == 10 and isinstance(int(corrected_isbn), int) and len(isbn) == 13:
                solution_list = []
                for index, num in enumerate(list(corrected_isbn[0:9]), 1):
                    solution_list.append(index * int(num))
                return sum(solution_list) % 11 == int(corrected_isbn[9])
            elif len(corrected_isbn) == 13 and isinstance(int(corrected_isbn), int) and len(isbn) == 17:
                solution_list = []
                for index, num in enumerate(list(corrected_isbn[0:12]), 1):
                    if index % 2 == 0:
                        solution_list.append(3 * int(num))
                    else:
                        solution_list.append(1 * int(num))
                solution_list_mod = sum(solution_list) % 10
                return solution_list_mod == int(corrected_isbn[12])
            else:
                return False
        except ValueError:
            return False


isbm = "0-306-40615-2"
print(Book.check_isbn(isbm))
isbm2 = "0306406152"
print(Book.check_isbn(isbm2))
isbm3 = "978-3-16-148410-0"
print(Book.check_isbn(isbm3))
isbm4 = "978-3-16-148410-0"
print(Book.check_isbn(isbm4))
isbm5 = "97a-3-16-148410-0"
print(Book.check_isbn(isbm5))
isbm6 = "0306406153"
print(Book.check_isbn(isbm6))
isbm7 = "978-83-7181-510-2"
print(Book.check_isbn(isbm7))
isbm8 = '978139316093'
print(Book.check_isbn(isbm8))

book = Book('Test Title', 'Test Author', '0306406152')
print(book.isbn)