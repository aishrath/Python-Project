from flask import Flask, render_template, request, url_for
import sqlite3 as sql
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ShoppingCart.html")
def get_shopping_cart():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM ShoppingCart"
    cur.execute(query)
    rows = cur.fetchall()
    return render_template("ShoppingCart.html", rows=rows)


@app.route("/Receipt.html")
def get_receipt():
    return render_template("Receipt.html")


@app.route("/Inventory.html")
def get_inventory():
    return render_template("Inventory.html")


@app.route("/changeDept.html")
def get_changeDept():
    return render_template("changeDept.html")


@app.route("/TotalInventory.html")
def get_total_inventory():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM Inventory"
    cur.execute(query)
    rows = cur.fetchall()
    return render_template("TotalInventory.html", rows=rows)

@app.route("/Produce.html")
def get_produce_inventory():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM Inventory WHERE Inventory.Kind='Produce'"
    cur.execute(query)
    rows = cur.fetchall()
    return render_template("Produce.html", rows=rows)

@app.route("/Seafood.html")
def get_seafood_inventory():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM Inventory WHERE Inventory.Kind='Seafood'"
    cur.execute(query)
    rows = cur.fetchall()
    return render_template("Seafood.html", rows=rows)

@app.route("/Electronics.html")
def get_electronics_inventory():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM Inventory WHERE Inventory.Kind='Electronics'"
    cur.execute(query)
    rows = cur.fetchall()
    return render_template("Electronics.html", rows=rows)

@app.route("/Household.html")
def get_household_inventory():
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    query = "SELECT Kind,Cost,Amount,Name FROM Inventory WHERE Inventory.Kind='Household'"
    cur.execute(query)
    rows = cur.fetchall()
    return render_template("Household.html", rows=rows)

@app.route("/Checkout.html")
def checkout():
    return render_template("Checkout.html")

def load_items(dept):
    con = sql.connect("groceryData.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    if(dept == "Produce"):
        query = "SELECT Name FROM Inventory WHERE Inventory.Kind ='Produce'"
    elif dept == "Seafood":
        query = "SELECT Name FROM Inventory WHERE Inventory.Kind ='Seafood'"
    elif dept == "Household":
        query = "SELECT Name FROM Inventory WHERE Inventory.Kind ='Household'"
    elif dept == "Electronics":
        query = "SELECT Name FROM Inventory WHERE Inventory.Kind ='Electronics'"

    cur.execute(query)
    rows = cur.fetchall()

    return render_template("addToCart.html", rows=rows, dept=dept)

def load_inventory():
    try:
       with sql.connect("groceryData.db") as con:
          cur = con.cursor()
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',1.00, 1000, 'Avocados')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',0.10, 1000, 'Bananas')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',1.50, 1000, 'Broccoli')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',0.70, 1000, 'Mangoes')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',0.05, 1000, 'Mushrooms')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',3.00, 1000, 'Bok Choy')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',1.75, 1000, 'Plantains')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',0.20, 1000, 'Oranges')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',0.50, 1000, 'Strawberries')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Produce',2.00, 1000, 'Mangoes')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',599.99,100,'Laptop')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',299.99,100,'Television')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',799.99,100,'Smartphone')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',50.00,100,'Printer')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',9.99,100,'Charger Cables')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',19.99,100,'Lightning Ports')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',9.99,100,'Mouse Pads')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',69.99,100,'Keyboard')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',359.99,100,'Game System')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Electronics',29.99,100,'Electronic Cleaner')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',15.99,250,'Pillows')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',29.99,250,'Blankets')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',99.99,250,'Paintings')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',40.00,250,'Plates')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',75.50,250,'Rugs')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',43.00,250,'Curtains')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',99.99,50,'Blinds')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',25.00,250,'Mirror')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',3000.00,250,'Statue')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Household',600.00,250,'Couch')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',10.00,25,'Shrimp')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',25.00,25,'Salmon')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',15.00,25,'Tilapia')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',250.00,10,'Caviar Bottle')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',5.00,250,'Seafood Rub')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',12.00,200,'Mussels')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',34.00,200,'Oysters')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',1.99,100,'Fish Sticks')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',9.99,25,'Fish Sauce')")
          cur.execute("INSERT INTO Inventory (Kind,Cost,Amount,Name) VALUES ('Seafood',47.00,20,'Eel')")
          con.commit()
          print("just commited")
    except:
       print("something went wrong")
       con.rollback()
    finally:
       con.close()

@app.route("/changeDept", methods=["POST", "GET"])
def changeDept():
    if request.method == "POST":
        try:
            depart = request.form["departments"]
        except:
            print("idk how u got here")
            pass

        finally:
            return load_items(depart)


@app.route("/addToCart", methods=["POST", "GET"])
def addToCart():
    if request.method == "POST":
        try:
            name = request.form["items"]
            amount = request.form["amount"]
            with sql.connect("groceryData.db") as con:
                cur = con.cursor()
                cur.execute("SELECT Cost,Kind FROM Inventory WHERE Inventory.Name= ?", (name,))
                hold = cur.fetchall()
                cost=hold[0][0]
                kind = hold[0][1]
                cur.execute("INSERT INTO ShoppingCart (Kind,Cost,Amount,Name,Tax) VALUES (?,?,?,?,?)",(kind,cost,int(amount),name,0.07))
                con.commit()
                #cur.execute("UPDATE Inventory"
                #            " SET Inventory.Amount = Inventory.Amount - ?", (amount),
                 #           "WHERE Inventory.Name =?",(name,))
                #con.commit()
                print("committed")
        except:
            print("something went wrong")
            con.rollback()
        finally:
            return render_template("changeDept.html")

if __name__ == "__main__":
    load_inventory()
    app.run(host="0.0.0.0")
