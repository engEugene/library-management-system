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

def menu():
   pass

def main():
    """Main function with a switch-like menu loop."""
    create_database()  # Ensure database is created before menu starts
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
