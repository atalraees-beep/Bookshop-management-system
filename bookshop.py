import json
import os
from abc import ABC, abstractmethod

# ===== ADMIN LOGIN =====
ADMIN_USERNAME = "atal"
ADMIN_PASSWORD = "1122"

def admin_login():
    for _ in range(3):
        u = input("Username: ")
        p = input("Password: ")
        if u == ADMIN_USERNAME and p == ADMIN_PASSWORD:
            print("Login Successful!\n")
            return True
        print("Invalid Credentials!")
    print("Access Denied!")
    return False


# ===== OOP MODEL =====
class Item(ABC):
    def __init__(self, book_id, title, price):
        self._book_id = book_id
        self._title = title
        self._price = price

    @abstractmethod
    def get_details(self):
        pass

    @property
    def price(self):
        return self._price


class Book(Item):
    def __init__(self, book_id, title, price):
        super().__init__(book_id, title, price)
        

    def get_details(self):
        return f"Book ID: {self._book_id} | {self._title} |  ${self._price}"


# ===== FILE STORAGE =====
class Storage:
    FILE = "books.json"

    @classmethod
    def load(cls):
        if not os.path.exists(cls.FILE):
            return []
        try:
            with open(cls.FILE, "r") as f:
                return json.load(f)
        except:
            return []

    @classmethod
    def save(cls, data):
        with open(cls.FILE, "w") as f:
            json.dump(data, f, indent=4)


# LOGIC
class BookShop:
    def __init__(self):
        self.books = Storage.load()

    def validate_price(self, price):
        if price <= 0:
            raise ValueError("Price must be positive")

    def add_book(self):
        try:
            i = int(input("Book ID: "))
            t = input("Title: ")
            p = float(input("Price: "))
            self.validate_price(p)

            self.books.append({
                "id": i,
                "title": t,
                "price": p,
            })

            Storage.save(self.books)
            print("Book Added Successfully!")
        except ValueError as e:
            print("Error:", e)

    def list_books(self):
        if not self.books:
            print("No Books Available.")
            return

        objects = []
        for book in self.books:
            obj = Book(book["id"], book["title"],
                        book["price"])
            objects.append(obj)

        for obj in objects:   # Polymorphism
            print(obj.get_details())

    def total_value(self):
        total = sum(book["price"] for book in self.books)
        print("Total Inventory Value:", total)


# MAIN MENU 
def main():
    shop = BookShop()

    while True:
        print("\n==== BOOKSHOP MENU ====")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Total Value")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            shop.add_book()
        elif choice == "2":
            shop.list_books()
        elif choice == "3":
            shop.total_value()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid Option!")


# ===== PROGRAM START =====
if __name__ == "__main__":
    print("=== ADMIN LOGIN REQUIRED ===")
    if admin_login():
        main()
