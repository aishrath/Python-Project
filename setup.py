import sqlite3

conn = sqlite3.connect('groceryData.db')

conn.execute('CREATE TABLE Inventory (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL)')
conn.execute('CREATE TABLE ShoppingCart (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL, Tax FLOAT)')
conn.execute('CREATE TABLE Receipt (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL, Tax FLOAT)')
conn.execute('CREATE TABLE Reviews (Name VARCHAR(50), Rating FLOAT, Review VARCHAR(500))')
conn.execute('CREATE TABLE Complaints (Complaint VARCHAR(500), Time DATETIME)')
conn.execute('CREATE TABLE Requests (Name VARCHAR(50), Kind VARCHAR(50))')

conn.commit()
conn.close()
