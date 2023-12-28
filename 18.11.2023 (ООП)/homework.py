class Book():
    def __init__(self, name, author, year, pages):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages
    def __str__(self):
        return f"Title: {self.name}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}"
    def show_info(self):
        print(f"Title: {self.name}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}")
book1 = Book("War and Peace", "Leo Tolstoy", 1869, 1225)
book2 = Book("The Witch Hunter", "Bernard Knight", 2004, 362 )

book1.show_info()
book2.show_info()
