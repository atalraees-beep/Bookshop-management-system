from abc import ABC, abstractmethod

# ---------- ABSTRACTION ----------
class BookBase(ABC):

    @abstractmethod
    def get_price(self):
        pass


# ---------- INHERITANCE ----------
class Book(BookBase):

    def __init__(self, book_id, title, price, stock):
        # ---------- ENCAPSULATION ----------
        self.__book_id = book_id
        self.title = title
        self.__price = price
        self.stock = stock

    # Getter (Encapsulation)
    def get_price(self):
        return self.__price

    def get_id(self):
        return self.__book_id

    def to_string(self):
        return f"{self.__book_id},{self.title},{self.__price},{self.stock}"

    @staticmethod
    def from_string(data):
        book_id, title, price, stock = data.strip().split(",")
        return Book(book_id, title, float(price), int(stock))


# ---------- POLYMORPHISM ----------
class PhysicalBook(Book):
    def get_price(self):
        return super().get_price() + 50  # delivery charges


# ---------- BUSINESS LOGIC ----------
def add_book():
    try:
        book_id = input("Book ID: ")
        title = input("Title: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))

        book = PhysicalBook(book_id, title, price, stock)
        (book)
        print(" Book added successfully!")

    except ValueError:
        print(" Invalid input!")


def view_books():
    books = ()
    if not books:
        print(" No books available")
        return

    for book in books:
        print(f"ID: {book.get_id()} | {book.title} | Price: {book.get_price()} | Stock: {book.stock}")


def sell_book():
    books = ()
    book_id = input("Enter Book ID to sell: ")
    updated = False

    for book in books:
        if book.get_id() == book_id:
            if book.stock > 0:
                book.stock -= 1
                updated = True
                print(" Book sold!")
            else:
                print(" Out of stock")

    if updated:
        try:
            with open("w") as file:
                for book in books:
                    file.write(book.to_string() + "\n")
        except IOError:
            print(" Error updating file")


# ---------- MAIN MENU ----------
def main():
    while True:
        print("\n Book Shop Menu")
        print("1. Add Book")
        print("2. View Books")
        print("3. Sell Book")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            sell_book()
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice")


# ---------- PROGRAM START ----------
    main()
