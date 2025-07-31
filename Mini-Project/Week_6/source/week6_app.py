# Import PostgreSQL adapter and OS/dotenv to load environment variables
import psycopg2 as psycopg
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database connection parameters from env file 
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

# === PRODUCT FUNCTIONS ===

def load_products(cursor):                                                    # Fetch and display all products from the database.
    print("\n=== Products ===")
    cursor.execute("SELECT id, product_name, product_price, product_type FROM products ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Price: £{row[2]}, Type: {row[3]}")


def add_product(cursor, connection):                                          # Prompts user for product info and insert new product into database.
    product_name = input("Product name: ")
    product_price = float(input("Product price: "))
    product_type = input("Product Type: ")
    
    cursor.execute("""
        INSERT INTO products (product_name, product_price, product_type)
        VALUES (%s, %s, %s)
        RETURNING id;
    """, (product_name, product_price, product_type))
    connection.commit()
    print(f"Added product with ID: {cursor.fetchone()[0]}")


def update_product(cursor, connection):                                       # Prompts user for product ID and new details, then updates the product.
    prod_id = int(input("Product ID to update: "))
    product_name = input("New Product Name: ")
    product_price = float(input("New Product Price: "))
    product_type = input("New Product Type: ")
    cursor.execute("""
        UPDATE products SET product_name=%s, product_price=%s, product_type=%s WHERE id=%s;
    """, (product_name, product_price, product_type, prod_id))
    connection.commit()
    print(f"Updated product ID: {prod_id}")


def delete_product(cursor, connection):                                        # Prompt user for product ID and deletes it from the database.
    prod_id = int(input("Product ID to delete: "))
    cursor.execute("DELETE FROM products WHERE id=%s;", (prod_id,))
    connection.commit()
    print(f"Deleted product ID: {prod_id}")

# === COURIER FUNCTIONS ===

def load_couriers(cursor):                                                    # Fetch and display all couriers from the database.
    print("\n=== Couriers ===")
    cursor.execute("SELECT courier_id, courier_name, courier_last_name, courier_company, courier_phone FROM couriers ORDER BY courier_id;")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Last Name: {row[2]}, Company: {row[3]}, Phone: {row[4]}")


def add_courier(cursor, connection):
    courier_name = input("Courier name: ")
    courier_last_name = input("Courier Last Name: ")                          # Prompt user for couriers info and inserts new courier into database.
    courier_company = input("Courier Company:")
    courier_phone = input("Courier phone: ")
    cursor.execute("""
        INSERT INTO couriers (courier_name, courier_last_name, courier_company, courier_phone)
        VALUES (%s, %s, %s, %s)
        RETURNING courier_id;
    """, (courier_name, courier_last_name, courier_company, courier_phone,))
    connection.commit()
    print(f"Added courier with ID: {cursor.fetchone()[0]}")


def update_courier(cursor, connection):
    courier_id = int(input("Courier ID to update: "))                        # Prompt user for couriers ID and new details, then updates the courier.
    courier_name = input("Courier name: ")
    courier_last_name = input("Courier Last Name: ")
    courier_company = input("Courier Company:")
    courier_phone = input("Courier phone: ")
    cursor.execute("""
        UPDATE couriers 
        SET courier_name=%s, courier_last_name=%s, courier_company=%s, courier_phone=%s 
        WHERE courier_id=%s;
    """, (courier_name, courier_last_name, courier_company, courier_phone, courier_id))
    connection.commit()
    print(f"Updated courier ID: {courier_id}")


def delete_courier(cursor, connection):
    courier_id = int(input("Courier ID to delete: "))                          # Prompt user for couriers ID and deletes it from the database.
    cursor.execute("DELETE FROM couriers WHERE courier_id=%s;", (courier_id,))
    connection.commit()
    print(f"Deleted courier ID: {courier_id}")

# === ORDER FUNCTIONS ===

def load_orders(cursor):
    print("\n=== Orders ===")                                                   # Fetch and display all orders from the database.    
    cursor.execute("""
        SELECT order_id, customer_name, customer_address, customer_phone, courier_id, ordered_item, status
        FROM orders ORDER BY order_id;
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Address: {row[2]}, Phone: {row[3]}, Courier ID: {row[4]}, Ordered Items: {row[6]}, Status: {row[5]}")


def add_order(cursor, connection):
    customer_name = input("Customer name: ")
    customer_address = input("Customer address: ")                             # Prompt user for order info and inserts new order into database.
    customer_phone = input("Customer phone: ")
    courier_id = int(input("Courier ID: "))
    ordered_item = int(input("Product ID: "))
    order_status = "Preparing"  # Default order status
    cursor.execute("""
        INSERT INTO orders (customer_name, customer_address, customer_phone, courier_id, ordered_item, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING order_id;
    """, (customer_name, customer_address, customer_phone, courier_id, ordered_item, order_status))
    connection.commit()
    print(f"Added order with ID: {cursor.fetchone()[0]}")


def update_order_status(cursor, connection): 
    order_id = int(input("Order ID to update: "))                               # Prompts user for order ID and new status, then updates the order status.
    order_status = input("New status: ")
    cursor.execute("""                                                      
        UPDATE orders SET status=%s WHERE order_id=%s;
    """, (order_status, order_id))
    connection.commit()
    print(f"Updated order ID: {order_id}")


def delete_order(cursor, connection):
    order_id = int(input("Order ID to delete: "))
    cursor.execute("DELETE FROM orders WHERE order_id=%s;", (order_id,))         #  Prompts user for order ID and deletes it from the database.
    connection.commit()
    print(f"Deleted order ID: {order_id}")

# === MAIN MENU ===

def main_app_menus():
    """Main application loop to navigate between menus and execute actions."""
    try:
        print("Opening connection...")
        with psycopg.connect(
            host=host_name,
            dbname=database_name,
            user=user_name,
            password=user_password
        ) as connection:

            print("Opening cursor...")
            cursor = connection.cursor()

            while True:
                # Main menu options
                print("\n--- Main Menu---")
                print("0. Exit")
                print("1. Products Menu")
                print("2. Couriers Menu")
                print("3. Orders Menu")
                
                main_menu_choice = input("Select an option: ")

                # Products submenu
                if main_menu_choice == "1":
                    print("\n--- Products Menu ---")
                    print("1. View Products")
                    print("2. Add Product")
                    print("3. Update Product")
                    print("4. Delete Product")
                    product_menu_choice = input("\nSelect an option: ")
                    if product_menu_choice == "1":
                        load_products(cursor)
                    elif product_menu_choice == "2":
                        add_product(cursor, connection)
                    elif product_menu_choice == "3":
                        update_product(cursor, connection)
                    elif product_menu_choice == "4":
                        delete_product(cursor, connection)

                # Couriers submenu
                elif main_menu_choice == "2":
                    print("\n--- Couriers Menu ---")
                    print("1. View Couriers")
                    print("2. Add Courier")
                    print("3. Update Courier")
                    print("4. Delete Courier")
                    courier_menu_choice = input("\nSelect an option: ")
                    if courier_menu_choice == "1":
                        load_couriers(cursor)
                    elif courier_menu_choice == "2":
                        add_courier(cursor, connection)
                    elif courier_menu_choice == "3":
                        update_courier(cursor, connection)
                    elif courier_menu_choice == "4":
                        delete_courier(cursor, connection)

                # Orders submenu
                elif main_menu_choice == "3":
                    print("\n--- Orders Menu ---")
                    print("1. View Orders")
                    print("2. Add Order")
                    print("3. Update Order Status")
                    print("4. Delete Order")
                    order_menu_choice = input("\nSelect an option: ")
                    if order_menu_choice == "1":
                        load_orders(cursor)
                    elif order_menu_choice == "2":
                        add_order(cursor, connection)
                    elif order_menu_choice == "3":
                        update_order_status(cursor, connection)
                    elif order_menu_choice == "4":
                        delete_order(cursor, connection)

                elif main_menu_choice == "0":
                    # Exit the application loop
                    break

            print("Closing cursor...")
            cursor.close()

    except Exception as e:
        print("Error:", e)

    print("All done!")

# Run the app if this file is executed directly
if __name__ == "__main__":
    main_app_menus()
