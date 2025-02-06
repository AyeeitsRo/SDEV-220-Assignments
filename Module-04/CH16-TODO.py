import csv
import sqlite3

'''Use the sqlite3 module to create a SQLite database
called books.db and a table called books with these fields: 
title (text), author (text), and year (integer).'''

with open('C:/Users/Its_R/Documents/SDEV 220/SDEV220-Repo/Module-04/books.csv', 'rt') as fin:
    cin = csv.reader(fin)
    books = [row for row in cin]
    
print(books)

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books(title VARCHAR(20) PRIMARY KEY,
             author VARCHAR(20), year INT)''')
ins = 'INSERT INTO books (title, author, year) VALUES(?, ?, ?)'
curs.execute(ins, ('The Weirdstone of Brisingamen', 'Alan Garner', 1960))
curs.execute(ins, ('Perdido Street Station', 'China Miéville', 2000))
curs.execute(ins, ('Thud!', 'Terry Pratchett', 2005))
curs.execute(ins, ('The Spellman Files', 'Lisa Lutz', 2007))
curs.execute(ins, ('Small Gods', 'Terry Pratchett', 1992))