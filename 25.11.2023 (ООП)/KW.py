class Book:
    def __init__(self, title, author, genre, number, get_ready):
        self.title = title
        self.author = author
        self.genre = genre
        self.number = number
        self.get_ready = get_ready
        self.book_list = []

    def get_info(self):
        return f"{self.title}, {self.author}, {self.genre}, {self.number}, {self.get_ready}"

class LendingLibray:
    def __init__(self, address, phone, email):
        self.address = address
        self.phone = phone
        self.email = email
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def delete_book(self, book):
        self.book_list.remove(book)

    def find(self, title):
        for name in self.book_list:
            if name.title == title:
                return name
            return "Not found"


class Patron:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available():
            book.available = False
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)


library = LendingLibray("г. Москва, ул. Пушкина, д. колотушкина", "8-800-123-45-67", "library@gmail.com")


book_1 = Book("War and Piece", "Lev Tolstoi", "roman", "3", False)
book_2 = Book("Meinkampf", "Adolf Hitler", "roman", "2", True)

user_1 = Patron("Larl", "TI12", "0-000-000-00-00", "team_spirit@mail.win")
user_2 = Patron("Yatoro", "TI12", "1-111-111-11-11", "team_spirit@mail.win")


library.add_book(book_1)
library.add_book(book_2)

print("Доступные книги:")
for book in library.book_list:
    if book.get_info():
        print(book.get_info())



print("Книги, выданные пользователю {}:".format(user_1.name))
for book in user_1.borrowed_books:
    print(book.get_info())

returned_book = input("Какую книгу вы хотите вернуть? ")
for book in user_1.borrowed_books:
    if book.get_info() == returned_book:
        user_1.return_book(book)
        break

print("Книги, выданные пользователю {}:".format(user_1.name))
for book in user_1.borrowed_books:
    print(book.get_title())

