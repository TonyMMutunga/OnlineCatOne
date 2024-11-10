class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"The book '{self.title}' has been marked as borrowed.")
        else:
            print(f"The book '{self.title}' is already borrowed.")

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"The book '{self.title}' has been marked as returned.")
        else:
            print(f"The book '{self.title}' is not currently borrowed.")


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Sorry, '{book.title}' is already borrowed by someone else.")
        else:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"'{book.title}' has been borrowed by {self.name}.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' to return.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"Books borrowed by {self.name}:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


# Interactive code to allow a member to borrow and return books
def main():
    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Create a library member
    member = LibraryMember("Alice", "M001")

    # Interact with the library system
    while True:
        print("\nLibrary System Menu:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available books:")
            for idx, book in enumerate([book1, book2, book3], start=1):
                status = "Available" if not book.is_borrowed else "Not Available"
                print(f"{idx}. {book.title} by {book.author} ({status})")
            book_choice = input("Enter the number of the book to borrow: ")
            
            try:
                selected_book = [book1, book2, book3][int(book_choice) - 1]
                member.borrow_book(selected_book)
            except (IndexError, ValueError):
                print("Invalid selection, please try again.")

        elif choice == "2":
            if not member.borrowed_books:
                print("You have no books to return.")
            else:
                print("Books you have borrowed:")
                for idx, book in enumerate(member.borrowed_books, start=1):
                    print(f"{idx}. {book.title} by {book.author}")
                return_choice = input("Enter the number of the book to return: ")

                try:
                    selected_book = member.borrowed_books[int(return_choice) - 1]
                    member.return_book(selected_book)
                except (IndexError, ValueError):
                    print("Invalid selection, please try again.")

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print("Exiting the Library System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the interactive library system
main()
