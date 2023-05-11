# Warehouse-management-app

This script provides a basic inventory management system that allows users to add, remove, and manage products and orders. The script uses SQLite to store the inventory data.


## Prerequisites

- Python 3.x
- SQLite3


## Usage

1. Clone the repository to your local machine.
2. Run the script `Warehouse Management App.py` in a Python environment.
3. Use the following functions to manage the inventory:
   - `add_product(name, price, quantity)`: Adds a new product to the inventory.
   - `delete_product(id)`: Removes a product from the inventory.
   - `add_order(date, product_id, quantity)`: Adds a new order to the inventory.
   - `display_products()`: Displays the list of products in the inventory.
   - `display_orders()`: Displays the list of orders in the inventory.


## Database schema

The database used by the script has two tables: `products` and `orders`.


The `products` table has the following columns:
  - `id`: The unique identifier of the product.
  - `name`: The name of the product.
  - `price`: The price of the product.
  - `quantity`: The quantity of the product in the inventory.


The `orders` table has the following columns:
  - `id`: The unique identifier of the order.
  - `date`: The date of the order.
  - `product_id`: The unique identifier of the product being ordered.
  - `quantity`: The quantity of the product being ordered.


## Exapmle  of usage

```python
import sqlite3

# Creating a database connection
conn = sqlite3.connect('inventory.db')

# Adding a new product to the inventory
add_product("Milk", 2.5, 100)

# Adding a new order to the inventory
add_order("2023-05-10", 1, 10)

# Displaying the list of products in the inventory
display_products()

# Displaying the list of orders in the inventory
display_orders()

# Removing a product from the inventory
delete_product(1)

# Closing the database connection
conn.close()
```
