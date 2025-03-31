import sqlite3

# Establish a connection to the database
CONN = sqlite3.connect("library_management.db")
CURSOR = CONN.cursor()
