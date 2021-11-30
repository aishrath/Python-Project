import sqlite3

conn = sqlite3.connect('groceryData.db')

conn.execute('CREATE TABLE Inventory (Kind VARCHAR(50), Cost DECIMAL, Amount INTEGER, Name VARCHAR(50))')
conn.execute('CREATE TABLE ShoppingCart (Kind VARCHAR(50), Cost DECIMAL, Amount INTEGER, Name VARCHAR(50), Tax FLOAT)')
conn.execute('CREATE TABLE Receipt (Kind VARCHAR(50), Cost DECIMAL, Amount INTEGER, Name VARCHAR(50), Tax FLOAT)')

conn.commit()
conn.close()
