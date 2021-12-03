from flask import Flask, render_template, request, url_for
import sqlite3 as sql
import datetime

app = Flask(__name__)


def dbInsert(table, kind, name, amount, cost, tax=-1):
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    if(tax == -1):
        cur.execute("INSERT INTO %s (Kind,Name,Amount,Cost) VALUES (?,?,?,?)" % table, (kind, name, amount, cost))
    else:
        cur.execute("INSERT INTO %s (Kind,Name,Amount,Cost,Tax) VALUES (?,?,?,?,?)" % table, (kind, name, amount, cost, tax))
    con.commit()
    con.close()


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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/Inventory.html")
def get_inventory():
    return render_template("Inventory.html")


@app.route("/Produce.html")
def get_produce_inventory():
    return render_template("Produce.html", rows=get_X_inventory("Produce"))


@app.route("/Household.html")
def get_household_inventory():
    return render_template("Household.html", rows=get_X_inventory("Household"))


@app.route("/Electronics.html")
def get_electronics_inventory():
    return render_template("Electronics.html", rows=get_X_inventory("Electronics"))


@app.route("/Seafood.html")
def get_seafood_inventory():
    return render_template("Seafood.html", rows=get_X_inventory("Seafood"))


@app.route("/TotalInventory.html")
def get_total_inventory():
    return render_template("TotalInventory.html", rows=get_X_inventory("TotalInventory"))


@app.route("/changeDept.html")
def get_changeDept():
    return render_template("changeDept.html")


@app.route("/ShoppingCart.html")
def get_shopping_cart():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Kind,Cost,Amount,Name FROM ShoppingCart")
    return render_template("ShoppingCart.html", rows=cur.fetchall())


@app.route("/Checkout.html")
def get_checkout():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Kind,Name,Amount,Cost,Tax FROM ShoppingCart")
    sub = tax = total = 0
    rows = cur.fetchall()
    for row in rows:
        sub += row["Cost"] * row["Amount"]
        tax += row["Cost"] * row["Amount"] * row["Tax"]
    total += sub + tax
    totals = (sub, tax, total)
    return render_template("Checkout.html", rows=rows, totals=totals)


@app.route("/Receipt.html")
def get_receipt():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT Kind,Name,Amount,Cost,Tax FROM Receipt")
    rows = cur.fetchall()
    sub = tax = total = 0
    for row in rows:
        sub += row["Cost"] * row["Amount"]
        tax += row["Cost"] * row["Amount"] * row["Tax"]
    total += sub + tax
    totals = (sub, tax, total)
    return render_template("Receipt.html", rows=cur.fetchall(), totals=totals)


def load_inventory():
    dbInsert("Inventory", "Produce", "Avocados", 1000, 1.00)
    dbInsert("Inventory", "Produce", "Bananas", 1000, 0.10)
    dbInsert("Inventory", "Produce","Broccoli", 1000, 1.50)
    dbInsert("Inventory", "Produce", "Mangoes", 1000, 0.70)
    dbInsert("Inventory", "Produce", "Mushrooms", 1000, 0.05)
    dbInsert("Inventory", "Produce", "Bok Choy", 1000, 3.00)
    dbInsert("Inventory", "Produce", "Plantains", 1000, 1.75)
    dbInsert("Inventory", "Produce", "Oranges", 1000, 0.20)
    dbInsert("Inventory", "Produce", "Strawberries", 1000, 0.50)
    dbInsert("Inventory", "Produce", "Mangoes", 1000, 2.00)
    dbInsert("Inventory", "Electronics", "Laptop", 100, 599.99)
    dbInsert("Inventory", "Electronics", "Television", 100, 299.99)
    dbInsert("Inventory", "Electronics", "Smartphone", 100, 799.99)
    dbInsert("Inventory", "Electronics", "Printer", 100, 50.00)
    dbInsert("Inventory", "Electronics", "Charger Cables", 100, 9.99)
    dbInsert("Inventory", "Electronics", "Lightning Ports", 100, 19.99)
    dbInsert("Inventory", "Electronics","Mouse Pads", 100, 9.99)
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


@app.route("/changeDept", methods=["POST", "GET"])
def changeDept():
    depart = None;
    if request.method == "POST":
        try:
            depart = request.form["departments"]
        except:
            print("Could not request.form[departments]")
            pass
        finally:
            if(depart is not None):
                return load_items(depart)
            else:
                print("Could not change department")


def load_items(dept):
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Name FROM Inventory WHERE Kind = '%s'" % dept if (dept != "") else ""
    if(query != ""):
        cur.execute(query)
        return render_template("addToCart.html", rows=cur.fetchall(), dept=dept)
    else:
        print("Could not load_items")
        return None;


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
                    dbInsert("ShoppingCart", row["Kind"], row["Name"], request.form[row["Name"]],
                             row["Cost"], 0.075 if (dept != "Produce" and dept != "Seafood") else 0)
                print("addedToCart")
        except:
            print("Could not addToCart")
            con.rollback()
        finally:
            return get_shopping_cart()


@app.route("/Checkout.html", methods=["POST", "GET"])
def checkout():
    if request.method == "POST":
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
        finally:
            if(cur is not None):
                cur.execute("SELECT Kind,Name,Amount,Cost,Tax FROM Receipt")
                rows = cur.fetchall()
                sub = tax = total = 0
                for row in rows:
                    sub += row["Cost"] * row["Amount"]
                    tax += row["Cost"] * row["Amount"] * row["Tax"]
                total += sub + tax
                totals = (sub, tax, total)
                return render_template("Receipt.html", rows=rows, totals=totals)
            print("Could not checkout")
            return render_template("Checkout.html")


if __name__ == "__main__":
    # If db empty, load_inventory()
    if not sql.connect("groceryData.db").cursor().execute("SELECT * FROM Inventory").fetchall():
        load_inventory()
    app.run(host="0.0.0.0")
