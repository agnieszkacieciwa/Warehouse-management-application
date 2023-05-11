import sqlite3

# Creating a database connection
conn = sqlite3.connect('inventory.db')

# Creating tables in the database
conn.execute('''CREATE TABLE IF NOT EXISTS products
                (id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 price REAL NOT NULL,
                 quantity INTEGER NOT NULL)''')

conn.execute('''CREATE TABLE IF NOT EXISTS orders
                (id INTEGER PRIMARY KEY,
                 date TEXT NOT NULL,
                 product_id INTEGER NOT NULL,
                 quantity INTEGER NOT NULL,
                 FOREIGN KEY (product_id) REFERENCES products(id))''')

# Function to add new products to the inventory
def add_product(name, price, quantity):
    conn.execute("INSERT INTO products name, price, quantity) VALUES (?, ?, ?)", name, price, quantity))
    conn.commit()

# Function to remove products from the inventory
def delete_product(id):
    conn.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()

# Function to manage orders
def add_order(date, product_id, quantity):
    conn.execute("INSERT INTO orders (date, product_id, quantity) VALUES (?, ?, ?)", (date, product_id, quantity))
    conn.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?", (quantity, product_id))
    conn.commit()

# Function to display information about products in the inventory
def display_products():
    cursor = conn.execute("SELECT id, name, price, quantity FROM products")
    for row in cursor:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Price: ", row[2])
        print("Quantity: ", row[3])

# Function to display information about orders
def display_orders():
    cursor = conn.execute("SELECT orders.id, orders.date, products.name, orders.quantity FROM orders JOIN products ON orders.product_id = products.id")
    for row in cursor:
        print("ID: ", row[0])
        print("Date: ", row[1])
        print("Product: ", row[2])
        print("Quantity: ", row[3])


# Closing the database connection
conn.close()
