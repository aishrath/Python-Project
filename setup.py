# Names: Bailey Carr, Tony Drouillard, Aishwareeya Rath
# FSUID: bfc19, tld19b, ar19c
# Due Date: December 3, 2021
# This project was completed on the group efforts of Bailey Carr, Tony Drouillar, and Aishwareeya Rath

#this entire program is purely meant for creation of tables and the database

import sqlite3

conn = sqlite3.connect('groceryData.db')

conn.execute('CREATE TABLE Inventory (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL)')
conn.execute('CREATE TABLE ShoppingCart (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL, Tax FLOAT)')
conn.execute('CREATE TABLE Receipt (Kind VARCHAR(50), Name VARCHAR(50), Amount INTEGER, Cost DECIMAL, Tax FLOAT)')
conn.execute('CREATE TABLE Reviews (Name VARCHAR(50), Rating FLOAT, Review VARCHAR(500))')
conn.execute('CREATE TABLE Complaints (Complaint VARCHAR(500), Issue VARCHAR(50))')
conn.execute('CREATE TABLE Requests (Name VARCHAR(50), Kind VARCHAR(50))')

conn.commit()
conn.close()
