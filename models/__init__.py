import sqlite3

CONN = sqlite3.connect('library_management.db')
CURSOR = CONN.cursor()