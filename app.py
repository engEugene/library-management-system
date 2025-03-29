import sqlite3

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

def add_book():
    """Adds a new book to the database."""
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        pages = int(input("Enter number of pages: "))
        
        conn = sqlite3.connect('library_management.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author, pages) VALUES (?, ?, ?)", 
                      (title, author, pages))
        conn.commit()
        print("Book added successfully!")
    except ValueError:
        print("Invalid input! Please enter valid details.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def delete_book():
    """Deletes a book from the database by its ID."""
    try:
        book_id = input("Enter the ID of the book to delete: ")
        
        if not book_id.isdigit():
            print("Please enter a valid numeric ID!")
            return
            
        conn = sqlite3.connect('library_management.db')
        cursor = conn.cursor()
        
        # First check if book exists
        cursor.execute("SELECT id FROM books WHERE id = ?", (book_id,))
        if not cursor.fetchone():
            print(f"No book found with ID {book_id}!")
            return
            
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        print(f"Book with ID {book_id} deleted successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def view_books():
    """Displays all books in the database."""
    try:
        conn = sqlite3.connect('library_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
        if not books:
            print("No books found in the database!")
            return
            
        print("\nList of Books:")
        print("ID  | Title                 | Author              | Pages")
        print("-" * 60)
        for book in books:
            print(f"{book[0]:<3} | {book[1]:<20} | {book[2]:<20} | {book[3]}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def menu():
    """Displays the main menu options."""
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. Delete a book")
    print("3. View all books")
    print("4. Exit")

def main():
    """Main function with a switch-like menu loop."""
    create_database()  # Ensure database is created before menu starts
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            view_books()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
