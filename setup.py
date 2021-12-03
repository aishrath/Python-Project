import sqlite3

conn = sqlite3.connect('groceryData.db')

conn.execute('CREATE TABLE Inventory (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL)')
conn.execute('CREATE TABLE ShoppingCart (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL, Tax FLOAT)')
conn.execute('CREATE TABLE Receipt (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL, Tax FLOAT)')

conn.commit()
conn.close()
