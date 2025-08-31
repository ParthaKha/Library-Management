class Library:
    book_list = []
    
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            return True
        return False
    
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            return True
        return False
    
    def view_book_info(self):
        status = "Available" if self.__availability else "Borrowed"
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Status: {status}")
    
    def get_book_id(self):
        return self.__book_id
    
    def get_title(self):
        return self.__title
    
    def is_available(self):
        return self.__availability

# Initialize some books manually
book1 = Book("1", "A", "Abc")
book2 = Book("2", "B", "aBc")
book3 = Book("3", "C", "abC")

# Menu system
def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\n=== All Books ===")
            for book in Library.book_list:
                book.view_book_info()
        
        elif choice == "2":
            book_id = input("Enter Book ID to borrow: ")
            found = False
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    found = True
                    if book.is_available():
                        if book.borrow_book():
                            print(f"Successfully borrowed '{book.get_title()}'")
                        else:
                            print("Error borrowing book")
                    else:
                        print("Error: Book is already borrowed")
                    break
            if not found:
                print("Error: Book ID not found")
        
        elif choice == "3":
            book_id = input("Enter Book ID to return: ")
            found = False
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    found = True
                    if not book.is_available():
                        if book.return_book():
                            print(f"Successfully returned '{book.get_title()}'")
                        else:
                            print("Error returning book")
                    else:
                        print("Error: Book is not currently borrowed")
                    break
            if not found:
                print("Error: Book ID not found")
        
        elif choice == "4":
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()