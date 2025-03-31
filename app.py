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

def menu():
    """Displays the menu options."""
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Exit")

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

def main():
    """Main function with a menu loop."""
    create_database()  # Ensure the database is created before using it
    
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            createBook()
        elif choice == "2":
            viewBooks()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
