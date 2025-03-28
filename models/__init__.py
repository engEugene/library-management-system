import sqlite3

CONN = sqlite3.connect('library_management_database')
cursor = CONN.cursor()