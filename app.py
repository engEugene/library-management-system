import sqlite3
from models.books import Book
def create_database():
    """Creates the database and books table if they don't exist."""
    conn = sqlite3.connect('library_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# def menu():
#     """Displays the main menu options for the library management system."""
#     print("\n" + "=" * 30)
#     print("LIBRARY MANAGEMENT SYSTEM")
#     print("=" * 30)
#     print("1. Add a new book")
#     print("2. Display all books")
#     print("3. Search a book")
#     print("4. Update book")
#     print("5. Delete book")
#     print("6. Exit")
#     print("=" * 30)

def createBook():
    """ Function for adding books with validation """
    while True:
        title = input("Enter book title: ").strip()
        if not title:
            print("Title cannot be empty. Please try again.")
            continue
        if not isinstance(title, str):
            print("Title must be a string. Please try again.")
            continue
        if not title.replace(" ", "").isalpha():
            print("Title must contain only letters and spaces. Please try again.")
            continue
        break

    while True:
        author = input("Enter book author: ").strip()
        if not author:
            print("Author cannot be empty. Please try again.")
            continue
        if not isinstance(author, str):
            print("Author must be a string. Please try again.")
            continue
        if not author.replace(" ", "").isalpha():
            print("Author name must contain only letters and spaces. Please try again.")
            continue
        break

    while True:
        try:
            pages = int(input("Enter number of pages: ").strip())
            if pages <= 0:
                raise ValueError
        except ValueError:
            print("Pages must be a positive integer. Please try again.")
            continue
        break

    new_book = Book.create(title, author, pages)
    print(f"Book created successfully: {new_book}")


def viewBooks():
    """Function to display all books"""
    books = Book.get_all()
    if books:
        print("\nList of Books:")
        for book in books:
            print(book)
    else:
        print("\nNo books found.")

def deleteBook():
    """Function to delete a book by title"""
    title = input("Enter the title of the book to delete: ").strip()
    book = Book.find_by_title(title)  # Assuming a method to find a book by title exists in the Book model

    if book:
        # Check if `book` is an object or an ID
        book_id = book.id if hasattr(book, 'id') else book

        confirm = input(f"Are you sure you want to delete the book '{book.title}'? (yes/no): ").strip().lower()
        if confirm == "yes":
            if Book.delete(book_id):  # Pass the correct ID
                print(f"Book '{book.title}' deleted successfully.")
            else:
                print(f"Failed to delete the book '{book.title}'.")
        else:
            print("Deletion canceled.")
    else:
        print(f"No book found with the title '{title}'.")

def login():
    """Login function to determine user role."""
    while True:
        print("\n" + "=" * 30)
        print("LOGIN to LIBRARY MANAGEMENT SYSTEM")
        print("=" * 30)
        print("1. Student")
        print("2. Librarian")
        print("3. Exit")
        print("=" * 30)

        choice = input("Enter your role (1 for Student, 2 for Librarian, 3 to Exit): ").strip()

        if choice == "1":
            return "student"
        elif choice == "2":
            return "librarian"
        elif choice == "3":
            print("Exiting program. Goodbye!")
            exit()
        else:
            print("Invalid choice! Please enter a valid option.")

def student_menu():
    """Displays the student menu options."""
    print("\n" + "=" * 30)
    print("STUDENT MENU")
    print("=" * 30)
    print("1. View all books")
    print("2. Search for a book")
    print("3. Exit to login")
    print("=" * 30)

def librarian_menu():
    """Displays the librarian menu options."""
    print("\n" + "=" * 30)
    print("LIBRARIAN MENU")
    print("=" * 30)
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Update book")
    print("5. Delete book")
    print("6. Exit to login")
    print("=" * 30)

def student_actions():
    """Handles student-specific actions."""
    while True:
        student_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            viewBooks()
        elif choice == "2":
            title = input("Enter the title of the book to search: ").strip()
            book = Book.find_by_title(title)  # Assuming this method exists
            if book:
                print(f"Book found: {book}")
            else:
                print("No book found with that title.")
        elif choice == "3":
            print("Returning to login...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

def librarian_actions():
    """Handles librarian-specific actions."""
    while True:
        librarian_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            createBook()
        elif choice == "2":
            viewBooks()
        elif choice == "3":
            title = input("Enter the title of the book to search: ").strip()
            book = Book.find_by_title(title)  # Assuming this method exists
            if book:
                print(f"Book found: {book}")
            else:
                print("No book found with that title.")
        elif choice == "4":
            print("Update book functionality not implemented yet.")  # Placeholder
        elif choice == "5":
            deleteBook()
        elif choice == "6":
            print("Returning to login...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

def main():
    """Main function with a menu loop."""
    create_database()  # Ensure the database is created before using it
    
    while True:
        role = login()

        if role == "student":
            student_actions()
        elif role == "librarian":
            librarian_actions()

if __name__ == "__main__":
    main()
