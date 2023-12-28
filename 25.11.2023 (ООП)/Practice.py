# EX num 1
class Product:
    def __int__(self, name: str, id: int, price: int, rating: int, stock: int):
        self.__name = name
        self.__id = id
        self.__price = price
        self.__rating = rating
        self.__stock = stock

    def add_stock(self, count):
        self.__stock += count

    def remove_stock(self, count):
        if self.__stock >= count:
            self.__stock -= count
        else:
            raise ValueError("Not enough stock available")

    def update_rating(self, new_rating):
        self.__rating = new_rating

    def update_price(self, new_price):
        self.__price = new_price

# EX num 2

class Category:
    def __int__(self, name: str, products):
        self.__name = name
        self.__products = []

    def add_item(self, item):
        self.__products += item

    def remove_item(self, item):
        for item in self.__products:
            if item == self.__name:
                self.__products.remove(item)
            else:
                raise ValueError("Not found")

    def __getitem__(self, item):
        for name in self.__products:
            if name == item:
                return name

category_1 = Category("Electronics")
category_2 = Category("Clothing")

# Ex num 3

class Basket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the basket")

    def get_items(self):
        return self.items

    def make_purchase(self, item_ids):
        purchased_items = []
        for item in self.items:
            if item.product_id in item_ids:
                purchased_items.append(item)
                self.items.remove(item)

        if purchased_items:
            print("Purchased items:")
            for item in purchased_items:
                print(item.name)
        else:
            print("No items purchased")

# Ex num 4

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.basket = Basket()