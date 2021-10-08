import sqlite3

conn = sqlite3.connect('groceryData.db')

conn.execute('CREATE TABLE Inventory (Kind CHAR, Cost DECIMAL, Amount INTEGER, Name CHAR PRIMARY KEY)')
conn.execute('CREATE TABLE ShoppingCart (Kind CHAR, Cost DECIMAL, Amount INTEGER, Name CHAR PRIMARY KEY, Tax FLOAT)')
conn.execute('CREATE TABLE Receipt (Kind CHAR, Cost DECIMAL, Amount INTEGER, Name CHAR PRIMARY KEY, Tax FLOAT)')
