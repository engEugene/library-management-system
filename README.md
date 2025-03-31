## Welcome to our Library Management System

## Description

The Library Management System is a command-line application built with Python and SQLite. It allows librarians to manage books in a library database while providing students with an easy way to search and view available books.

## Features

Librarian functionalities:

1. Add new books

2. View all books

3. Search for books

4. Update book details

5. Delete books

Student functionalities:

1. View all books

2. Search for books

Technologies Used

Python

SQLite

## Setup Instructions

## Prerequisites

Ensure you have the following installed on your system: Python, SQLite Python Library

## Installation Steps

Clone the repository:

1. `git clone <https://github.com/engEugene/library-management-system>`
2. `cd library-management-system`

Before you run our application, install necessary dependencies using pipenv:

`pip install pipenv`
`pipenv install`

## Finally run the application:

python app.py

## Usage

On running app.py, you will be prompted to log in as a Student or Librarian.

Students can search and view books.

Librarians can manage books (add, update, delete, and view all books).

## Database Structure

The application uses an SQLite database with the following table:

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    pages INTEGER NOT NULL
);

## Contributing

If you want to contribute:

1. Fork the repository

2. Create a new branch (git checkout -b feature-branch)

3. Commit your changes (git commit -m "Added a new feature")

4. Push to the branch (git push origin feature-branch)

5. Open a Pull Request