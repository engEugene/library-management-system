from models import CURSOR, CONN

class Book:
    all = {}

    def __init__(self, title, author, pages, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', pages={self.pages})"

    """
        PROPERTY METHODS
    """
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._author = value
        else:
            raise ValueError("Author must be a non-empty string")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Pages must be a positive integer")

    """
        ORM CLASS METHODS
    """
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                pages INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS books;"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, title, author, pages):
        new_book = cls(title, author, pages)
        new_book.save()
        return new_book

    @classmethod
    def instance_from_db(cls, result):
        if book := cls.all.get(result[0]):
            book.title = result[1]
            book.author = result[2]
            book.pages = result[3]
        else:
            book = cls(result[1], result[2], result[3], id=result[0])
            cls.all[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books;"
        results = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(result) for result in results]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM books WHERE id = ?;"
        result = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(result) if result else None

    @classmethod
    def find_by_title(cls, title):
        sql = "SELECT * FROM books WHERE title = ?;"
        result = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(result) if result else None

    """
        ORM CRUD INSTANCE METHODS
    """
    def save(self):
        sql = "INSERT INTO books (title, author, pages) VALUES (?, ?, ?);"
        CURSOR.execute(sql, (self.title, self.author, self.pages))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE books SET title = ?, author = ?, pages = ? WHERE id = ?;"
        CURSOR.execute(sql, (self.title, self.author, self.pages, self.id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM books WHERE id = ?;"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
