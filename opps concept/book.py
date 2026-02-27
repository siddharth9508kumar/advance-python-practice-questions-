<<<<<<< HEAD
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def discount_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        print(f"Discounted price: {discounted_price}")
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book1.display_info()
book1.price = 20.0
book1.discount_price(10)
=======
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def discount_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        print(f"Discounted price: {discounted_price}")
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book1.display_info()
book1.price = 20.0
book1.discount_price(10)
>>>>>>> 4c79a0f634310d5ee974a5ee537d7f8d183c6b03
