# Names: Bailey Carr, Tony Drouillard, Aishwareeya Rath
# FSUID: bfc19, tld19b, ar19c
# Due Date: December 3, 2021
# This project was completed on the group efforts of Bailey Carr, Tony Drouillar, and Aishwareeya Rath

# These are various libraries we needed for the project
# flask gives us ability to interact with the user through HTML
# sqlite3 gives us interaction with the database
# datetime allows us to get the current date and time
# randint allows us to get the number of the day of the week
from flask import Flask, render_template, request, url_for
import sqlite3 as sql
import datetime
from random import randint

app = Flask(__name__)

# a function we wrote to streamline inserts into the database
def dbInsert(table, kind, name, amount, cost, tax=-1):
    con = sql.connect("groceryData.db")
    cur = con.cursor()
    alreadyExists = cur.execute("SELECT Amount FROM %s WHERE Name=?" % table, (name,)).fetchone()
    if(alreadyExists):
        cur.execute("UPDATE {0} SET Amount={1} WHERE Name='{2}'".format(table, int(alreadyExists[0])+int(amount), name))
    else:
        if(tax == -1):
            cur.execute("INSERT INTO %s (Kind,Name,Amount,Cost) VALUES (?,?,?,?)" % table, (kind, name, amount, cost))
        else:
            cur.execute("INSERT INTO %s (Kind,Name,Amount,Cost,Tax) VALUES (?,?,?,?,?)" % table, (kind, name, amount, cost, tax))
    con.commit()
    con.close()

# a function written to assist with grabbing things from the inventory we have, if it is not the total inventory
# if it is the total inventory, we just grab the whole entire inventory
def get_X_inventory(kind):
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM Inventory"
    query += " WHERE Kind='%s'" % kind if (kind != "TotalInventory") else ""
    cur.execute(query)
    rows = cur.fetchall()
    con.close()
    return rows

# renders the homepage
@app.route("/")
def home():
    return render_template("index.html")

# renders the main inventory page, from here the user can go to different inventories based off of what kind of
# product they would like to buy. They can also view all products in one list through a link on this page
@app.route("/Inventory.html")
def get_inventory():
    return render_template("Inventory.html")

# renders the produce inventory
@app.route("/Produce.html")
def get_produce_inventory():
    return render_template("Produce.html", rows=get_X_inventory("Produce"))

# renders the household inventory
@app.route("/Household.html")
def get_household_inventory():
    return render_template("Household.html", rows=get_X_inventory("Household"))

# renders the electronics inventory
@app.route("/Electronics.html")
def get_electronics_inventory():
    return render_template("Electronics.html", rows=get_X_inventory("Electronics"))

# renders the seafood inventory
@app.route("/Seafood.html")
def get_seafood_inventory():
    return render_template("Seafood.html", rows=get_X_inventory("Seafood"))

# renders all products in the inventory
@app.route("/TotalInventory.html")
def get_total_inventory():
    return render_template("TotalInventory.html", rows=get_X_inventory("TotalInventory"))

# this grabs all the products the user currently has sitting inside of their shopping cart and displays it
# to them on the shopping cart page
@app.route("/ShoppingCart.html")
def get_shopping_cart():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Kind,Cost,Amount,Name FROM ShoppingCart")
    rows = cur.fetchall()
    con.close()
    return render_template("ShoppingCart.html", rows=rows)

# This page displays the checkout totals of everything the user has in their cart
# we have also added "sales" for each day of the week. This day of the week is generated
# by a random number generator from 1 to 7. The corresponding day and sale amount is shown
@app.route("/Checkout.html")
def get_checkout():
# we have to make randnum from the randnum est in main, so it is the global randnum
    global randnum
    print(randnum)
    print("just got randnum")
# decides the sale and the day of the week
    if randnum == 1:
       day = "Sunday"
       sale = 0.95
    elif randnum == 2:
       day = "Monday"
       sale = 0.85
    elif randnum == 3:
       day = "Tuesday"
       sale = 0.90
    elif randnum == 4:
       day = "Wednesday"
       sale = 0.75
    elif randnum == 5:
       day = "Thursday"
       sale = 0.80
    elif randnum == 6:
       day = "Friday"
       sale = 0.90
    elif randnum == 7:
       day = "Saturday"
       sale = 0.95
    else:
        day = "A Normal Day"
        sale = 1
# grabs the sale amount as a percent
    discount = 1 - sale
    discount = round(discount, 2)
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Kind,Name,Amount,Cost,Tax FROM ShoppingCart")
    sub = tax = total = 0
    rows = cur.fetchall()
# calculates the cost with the sale factored in
    for row in rows:
        sub += row["Cost"] * row["Amount"] * sale
        tax += row["Cost"] * row["Amount"] * row["Tax"]
    total += sub + tax
    totals = (sub, tax, total)
    con.close()
    return render_template("Checkout.html", day=day, sale=discount*100,rows=rows, totals=totals)

# users can request products through this page
@app.route("/RequestProduct.html")
def add_request():
    return render_template("RequestProduct.html")

# users can see other users' requests through this page
@app.route("/ShowRequests.html")
def show_requests():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Requests")
    rows = cur.fetchall()
    con.close()
    return render_template("ShowRequests.html", rows=rows)

# if a user wants to add their review, this page will show
@app.route("/AddReview.html")
def add_review():
    return render_template("AddReview.html")

# users can see everyone's review from this page
@app.route("/ShowReviews.html")
def show_reviews():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Reviews")
    rows = cur.fetchall()
    con.close()
    return render_template("ShowReviews.html", rows=rows)

# this page generates the receipt for the products that the user has purchased
# once again the random number is chose through that global randnum
@app.route("/Receipt.html")
def get_receipt():
    global randnum
    print(randnum)
    print("just got randnum")
    if randnum == 1:
        sale = 0.95
    elif randnum == 2:
        sale = 0.85
    elif randnum == 3:
        sale = 0.90
    elif randnum == 4:
        sale = 0.75
    elif randnum == 5:
        sale = 0.80
    elif randnum == 6:
        sale = 0.90
    elif randnum == 7:
        sale = 0.95
    else:
        sale = 1
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Kind,Name,Amount,Cost,Tax FROM Receipt")
    rows = cur.fetchall()
    sub = tax = total = 0
    for row in rows:
        sub += row["Cost"] * row["Amount"] * sale
        tax += row["Cost"] * row["Amount"] * row["Tax"]
    total += sub + tax
    totals = (sub, tax, total)
    con.close()
    return render_template("Receipt.html", rows=rows, totals=totals)

# this grabs the data the user submitted from the add review page and just adds it
# to the appropirate table in the database
@app.route("/addReview", methods=["POST", "GET"])
def addReview():
    if request.method == "POST":
        try:
            name = request.form["Name"]
            rating = request.form["Rating"]
            review = request.form["Review"]
            with sql.connect("groceryData.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Reviews (Name,Rating,Review) VALUES (?,?,?)", (name, rating, review))
                con.commit()
        except:
            con.rollback()
            con.close()
            return render_template("index.html")
        else:
            con.close()
            return show_reviews()

# same as above, grabs the users wishes and adds it to the right tabel
@app.route("/requestProduct", methods=["POST", "GET"])
def requestProduct():
    if request.method == "POST":
        try:
            name = request.form["Name"]
            kind = request.form["Kind"]
            with sql.connect("groceryData.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Requests (Name,Kind) VALUES (?,?)", (name, kind))
                con.commit()
        except:
            con.rollback()
            con.close()
            return render_template("index.html")
        else:
            con.close()
            return show_requests()

# if a user has complaints :( they can add their complaints and the approrpiate page is rendered
@app.route("/Complaints.html")
def get_complaint_form():
    con = sql.connect("groceryData.db")
    cur = con.cursor()
    cur.execute("SELECT Kind FROM Inventory")
    rows = cur.fetchall()
    return render_template("Complaints.html",rows=rows)

# grabs data from the complaints page and add it to the table
@app.route("/file_complaint", methods=["POST", "GET"])
def file_complaint():
    if request.method == "POST":
        try:
            print("entering try")
            complaint = request.form["Complaint"]
            print("complaint is ", complaint)
            issue = request.form["Issue"]
            print("time is ", issue)
            with sql.connect("groceryData.db") as con:
                print("entering connect")
                cur = con.cursor()
                cur.execute("INSERT INTO Complaints (Complaint,Issue) VALUES (?,?)", (complaint, issue))
                con.commit()
        except:
            print("except")
            con.rollback()
        finally:
            return render_template("index.html")

# we have hard coded 40 products, 10 per kind
def load_inventory():
    dbInsert("Inventory", "Produce", "Avocados", 1000, 1.00)
    dbInsert("Inventory", "Produce", "Bananas", 1000, 0.10)
    dbInsert("Inventory", "Produce", "Broccoli", 1000, 1.50)
    dbInsert("Inventory", "Produce", "Mangoes", 1000, 0.70)
    dbInsert("Inventory", "Produce", "Mushrooms", 1000, 0.05)
    dbInsert("Inventory", "Produce", "Bok Choy", 1000, 3.00)
    dbInsert("Inventory", "Produce", "Plantains", 1000, 1.75)
    dbInsert("Inventory", "Produce", "Oranges", 1000, 0.20)
    dbInsert("Inventory", "Produce", "Strawberries", 1000, 0.50)
    dbInsert("Inventory", "Produce", "Beans", 1000, 2.00)
    dbInsert("Inventory", "Electronics", "Laptop", 100, 599.99)
    dbInsert("Inventory", "Electronics", "Television", 100, 299.99)
    dbInsert("Inventory", "Electronics", "Smartphone", 100, 799.99)
    dbInsert("Inventory", "Electronics", "Printer", 100, 50.00)
    dbInsert("Inventory", "Electronics", "Charger Cables", 100, 9.99)
    dbInsert("Inventory", "Electronics", "Lightning Ports", 100, 19.99)
    dbInsert("Inventory", "Electronics", "Mouse Pads", 100, 9.99)
    dbInsert("Inventory", "Electronics", "Keyboard", 100, 69.99)
    dbInsert("Inventory", "Electronics", "Game System", 100, 359.99)
    dbInsert("Inventory", "Electronics", "Electronic Cleaner", 100, 29.99)
    dbInsert("Inventory", "Household", "Pillows", 250, 15.99)
    dbInsert("Inventory", "Household", "Blankets", 250, 29.99)
    dbInsert("Inventory", "Household", "Paintings", 250, 99.99)
    dbInsert("Inventory", "Household", "Plates", 250, 40.00)
    dbInsert("Inventory", "Household", "Rugs", 250, 75.50)
    dbInsert("Inventory", "Household", "Curtains", 250, 43.00)
    dbInsert("Inventory", "Household", "Blinds", 50, 99.99)
    dbInsert("Inventory", "Household", "Mirror", 250, 25.00)
    dbInsert("Inventory", "Household", "Statue", 250, 3000.00)
    dbInsert("Inventory", "Household", "Couch", 250, 600.00)
    dbInsert("Inventory", "Seafood", "Shrimp", 25, 10.00)
    dbInsert("Inventory", "Seafood", "Salmon", 25, 25.00)
    dbInsert("Inventory", "Seafood", "Tilapia", 25, 15.00)
    dbInsert("Inventory", "Seafood", "Caviar Bottle", 10, 250.00)
    dbInsert("Inventory", "Seafood", "Seafood Rub", 250, 5.00)
    dbInsert("Inventory", "Seafood", "Mussels", 200, 12.00)
    dbInsert("Inventory", "Seafood", "Oysters", 200, 34.00)
    dbInsert("Inventory", "Seafood", "Fish Sticks", 100, 1.99)
    dbInsert("Inventory", "Seafood", "Fish Sauce", 25, 9.99)
    dbInsert("Inventory", "Seafood", "Eel", 20, 47.00)
    print("load_inventory committed")

# this is how the products actually get added into the table
# we have drop downs next to each thing inside of the table they can see when trying to purchase something
# they can go to the appropriate button, add however much they want, and then it'll be added to
# their shopping cart and that much is removed from the inventory
@app.route("/addToCart", methods=["POST", "GET"])
def addToCart():
    if request.method == "POST":
        try:
            with sql.connect("groceryData.db") as con:
                dept = request.form["addToCart"]
                rows = get_X_inventory(dept)
                for row in rows:
                    if(request.form[row["Name"]] == "0"):
                        continue
                    # Add to Cart
                    dbInsert("ShoppingCart", row["Kind"], row["Name"], request.form[row["Name"]],
                             row["Cost"], 0.075 if (dept != "Produce" and dept != "Seafood") else 0)
                    # Update Inventory
                    dbInsert("Inventory", row["Kind"], row["Name"], -int(request.form[row["Name"]]), row["Cost"],
                             0.075 if (dept != "Produce" and dept != "Seafood") else 0)
                print("addedToCart")
        except:
            print("Could not addToCart")
            con.rollback()
        finally:
            con.close()
            return get_shopping_cart()

# when the user wants to checkout, this page will get them their sale amount and 
# render the appropriate page after performing the calculations necessary
@app.route("/Checkout.html", methods=["POST", "GET"])
def checkout():
    if request.method == "POST":
        global randnum
        if randnum == 1:
            sale = 0.95
        elif randnum == 2:
            sale = 0.85
        elif randnum == 3:
            sale = 0.90
        elif randnum == 4:
            sale = 0.75
        elif randnum == 5:
            sale = 0.80
        elif randnum == 6:
            sale = 0.90
        elif randnum == 7:
            sale = 0.95
        else:
            sale = 1
        try:
            with sql.connect("groceryData.db") as con:
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("DELETE FROM Receipt")
                cur.execute("INSERT INTO Receipt SELECT * FROM ShoppingCart")
                cur.execute("DELETE FROM ShoppingCart")
                con.commit()
                print("checkout Committed")
        except:
            print("Could not checkout")
            con.rollback()
            con.close()
            return render_template("index.html")
        else:
            cur.execute("SELECT * FROM Receipt")
            rows = cur.fetchall()
            sub = tax = total = 0
            for row in rows:
                # Calculate Receipt values
                sub += row["Cost"] * row["Amount"] * sale
                tax += row["Cost"] * row["Amount"] * row["Tax"]
            total += sub + tax
            totals = (sub, tax, total)
            return render_template("Receipt.html", rows=rows, totals=totals)

# just a main to actually get the program running
if __name__ == "__main__":
    # If db empty, load_inventory()
    if not sql.connect("groceryData.db").cursor().execute("SELECT * FROM Inventory").fetchone():
        load_inventory()
    randnum = randint(1, 7)
    print(randnum)
    app.run(host="0.0.0.0")

