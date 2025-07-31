import csv

# Data structures with pre-determined items converted to dictionaries

products = [
    {"name": "Americano", "price": 2.50, "type": "drink"},
    {"name": "Latte", "price": 3.00, "type": "drink"},
    {"name": "Mocha", "price": 3.20, "type": "drink"},
    {"name": "Hot Chocolate", "price": 2.80, "type": "drink"},
    {"name": "Iced Coffee", "price": 3.00, "type": "drink"},
    {"name": "Flat White", "price": 3.10, "type": "drink"},                 # Stores product info as dictionaries with name, price and type 
    {"name": "Espresso", "price": 2.00, "type": "drink"},                                         
    {"name": "Croissant", "price": 1.80, "type": "food"},
    {"name": "Panini", "price": 4.50, "type": "food"},
    {"name": "Muffin", "price": 2.20, "type": "food"},
    {"name": "Toastie", "price": 3.80, "type": "food"},
    {"name": "Brownie", "price": 2.50, "type": "food"},
    {"name": "Choc Chip Cookie", "price": 1.50, "type": "food"}
]

couriers = [
    {"name": "Deliveroo", "phone": "020 1234 5678"},
    {"name": "Just Eat", "phone": "020 2345 6789"},
    {"name": "Uber Eats", "phone": "020 3456 7890"},
    {"name": "Costa Coffee", "phone": "020 4567 8901"},                     # Stores courier info with name and phone number 
    {"name": "Starbucks", "phone": "020 5678 9012"},
    {"name": "Pret-A-Manger", "phone": "020 6789 0123"},
    {"name": "Greggs", "phone": "020 7890 1234"}
]
# Stores all orders and status options 
orders = []
order_status_options = ["PREPARING", "DISPATCHED", "OUT FOR DELIVERY", "DELIVERED"]          

# File names for data persistence 
products_file = "products.csv"
couriers_file = "couriers.csv"
orders_file = "orders.csv"

# CSV Loading Functions (updated to handle pre-loaded data)
def load_products():
    try:
        with open(products_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames:  # Only clear if file has data
                products.clear()
                for row in reader:
                    if row:
                        row['price'] = float(row['price'])
                        products.append(row)
    except FileNotFoundError:
        print(f"Warning: {products_file} not found. Using default products.")

def load_couriers():
    try:
        with open(couriers_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames:  # Only clear if file has data
                couriers.clear()
                for row in reader:
                    if row:
                        couriers.append(row)
    except FileNotFoundError:
        print(f"Warning: {couriers_file} not found. Using default couriers.")

def load_orders():    # Function loads persisted data for orders from the orders.csv file 
    try:
        with open(orders_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            orders.clear()
            for row in reader:
                if row:
                    row['courier'] = int(row['courier']) if 'courier' in row and row['courier'].isdigit() else -1
                    orders.append(row)
    except FileNotFoundError:    # Error exception for if orders.csv file has nothing stored inside and prints statement out letting the user know 
        print(f"Warning: {orders_file} not found. Starting with empty orders list.")

# CSV Saving Functions (updated)
def save_products():    # Function saves data to a products.csv file when application is exited 
    with open(products_file, mode='w', newline='') as file:
        if products:
            fieldnames = products[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for product in products:
                writer.writerow(product)

def save_couriers():   # Function saves data to a couriers.csv file when application is exited 
    with open(couriers_file, mode='w', newline='') as file:
        if couriers:
            fieldnames = couriers[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for courier in couriers:
                writer.writerow(courier)

def save_orders():     # Function saves data to a orders.csv file when application is exited 
    with open(orders_file, mode='w', newline='') as file:
        if orders:
            fieldnames = orders[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for order in orders:
                writer.writerow(order)

# Order Functions (unchanged)
def print_order_menu():   # Function that prints an order menu when called upon later in the code (Line 207)
    print("\n--- Order Menu ---")
    print("0. Return to Main Menu")
    print("1. View All Orders")
    print("2. Add New Order")
    print("3. Update Order Status")
    print("4. Update Order Info")
    print("5. Delete Order")

def print_orders():     # Function to view all orders and can be called upon whenever order menu is needed to show up (Lines 172, 194, 207, 213)
    if not orders:
        print("\nNo orders found.")  # If statement used so that if there are no current orders the program will then print that there are no orders. 
    else:
        print("\n--- Current Orders ---")   # Else statement used so that if there are current orders the program will print out the orders dispalying the users( Name | Address | Phone Number | Assigned Courier | Order Status. ) 
        for idx, order in enumerate(orders):
            courier_idx = order.get("courier", -1)
            courier_name = couriers[courier_idx]['name'] if 0 <= courier_idx < len(couriers) else "Unknown"
            print(f"{idx}: Name: {order.get('customer_name', 'Unknown')} | " 
                  f"Address: {order.get('customer_address', 'Unknown')} | "
                  f"Phone: {order.get('customer_phone', 'Unknown')} | "
                  f"Courier: {courier_name} | "
                  f"Status: {order.get('status', 'Unknown')}")

def add_order():   # Function to add orders to the order menu containing users ( Name | Address | Phone Number | Assisgned Courier) that can be called upon later to print out code within the function
    name = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")
    phone = input("Enter Customer Phone Number: ")
    
    print("\nAvailable Products:")
    for idx, product in enumerate(products):
        print(f"{idx}: {product['name']} - £{product['price']:.2f}")
    
    product_indices = input("\nEnter product numbers (comma separated): ").split(',')  # (Newly added) when adding an order can now add products to the users order 
    products_ordered = []
    for idx in product_indices:
        try:
            idx = int(idx.strip())
            if 0 <= idx < len(products):
                products_ordered.append(products[idx]['name'])
        except ValueError:
            pass
    
    print("\nAvailable Couriers:")
    for idx, courier in enumerate(couriers):
        print(f"{idx}: {courier['name']} - {courier['phone']}")
    
    try:
        courier_idx = int(input("\nEnter courier number: "))
        if 0 <= courier_idx < len(couriers):
            new_order = {
                'customer_name': name,
                'customer_address': address,
                'customer_phone': phone,
                'products': ", ".join(products_ordered),
                'courier': courier_idx,
                'status': "PREPARING"
            }
            orders.append(new_order)
            print("\nOrder added successfully!")
        else:
            print("\nInvalid courier selection!")
    except ValueError:
        print("\nPlease enter a valid number!")

def update_order_status():
    if not orders:
        print("\nNo Orders To Update")
        return
    
    print_orders()
    try:
        order_index = int(input("\nEnter order number to update: "))
        if 0 <= order_index < len(orders):
            print("\nStatus Options:")
            for idx, status in enumerate(order_status_options):
                print(f"{idx}: {status}")
            
            status_index = int(input("Enter new status number: "))
            if 0 <= status_index < len(order_status_options):
                orders[order_index]['status'] = order_status_options[status_index]
                print("\nStatus updated!")
            else:
                print("\nInvalid status number!")
        else:
            print("\nInvalid order number!")
    except ValueError:
        print("\nPlease enter a valid number!")

def update_order_details():
    if not orders:
        print("\nNo Orders Available!")
        return
    
    print_orders()
    try:
        order_index = int(input("\nEnter order number to update: "))
        if 0 <= order_index < len(orders):
            order = orders[order_index]
            print("\nLeave blank to keep current value")
            for key in order:
                if key != 'courier' and key != 'status' and key != 'products':
                    new_value = input(f"{key} [{order[key]}]: ").strip()
                    if new_value:
                        order[key] = new_value
            print("\nOrder updated!")
        else:
            print("\nInvalid order number!")
    except ValueError:
        print("\nPlease enter a valid number!")

def delete_order():
    if not orders:
        print("\nNo Orders To Delete!")
        return
    
    print_orders()
    try:
        order_index = int(input("\nEnter order number to delete: "))
        if 0 <= order_index < len(orders):
            deleted_order = orders.pop(order_index)
            print(f"\nOrder for {deleted_order['customer_name']} deleted!")
        else:
            print("\nInvalid order number!")
    except ValueError:
        print("\nPlease enter a valid number!")

def handle_order_menu():
    while True:
        print_order_menu()
        choice = input("\nSelect an option: ")
        
        if choice == "0":
            break
        elif choice == "1":
            print_orders()
        elif choice == "2":
            add_order()
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            update_order_details()
        elif choice == "5":
            delete_order()
        else:
            print("Invalid choice. Please try again.")

# Courier Functions (updated for WEEK 4)
def print_courier_menu():
    print("\n--- Courier Menu ---")
    print("0. Return to Main Menu")
    print("1. View All Couriers")
    print("2. Add New Courier")
    print("3. Update Courier")
    print("4. Delete Courier")

def handle_courier_menu():
    while True:
        print_courier_menu()
        choice = input("\nSelect an option: ")
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n--- Couriers List ---")
            for idx, courier in enumerate(couriers):
                print(f"{idx}: {courier['name']} - {courier['phone']}")
        elif choice == "2":
            name = input("\nEnter courier name: ").strip()
            while not name:
                print("Name cannot be empty")
                name = input("Enter courier name: ").strip()
            
            phone = input("Enter courier phone: ").strip()
            while not phone:
                print("Phone cannot be empty")
                phone = input("Enter courier phone: ").strip()
            
            couriers.append({"name": name, "phone": phone})
            print(f"\nCourier '{name}' added successfully!")
        elif choice == "3":
            if not couriers:
                print("\nNo couriers available to update")
                continue
            
            print("\n--- Couriers List ---")
            for idx, courier in enumerate(couriers):
                print(f"{idx}: {courier['name']} - {courier['phone']}")
            
            try:
                courier_idx = int(input("\nEnter courier number to update: "))
                if 0 <= courier_idx < len(couriers):
                    courier = couriers[courier_idx]
                    print("\nLeave blank to keep current value")
                    
                    new_name = input(f"Name [{courier['name']}]: ").strip()
                    if new_name:
                        courier['name'] = new_name
                    
                    new_phone = input(f"Phone [{courier['phone']}]: ").strip()
                    if new_phone:
                        courier['phone'] = new_phone
                    
                    print("\nCourier updated successfully!")
                else:
                    print("\nInvalid courier number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        elif choice == "4":
            if not couriers:
                print("\nNo couriers available to delete")
                continue
            
            print("\n--- Couriers List ---")
            for idx, courier in enumerate(couriers):
                print(f"{idx}: {courier['name']} - {courier['phone']}")
            
            try:
                courier_idx = int(input("\nEnter courier number to delete: "))
                if 0 <= courier_idx < len(couriers):
                    deleted = couriers.pop(courier_idx)
                    print(f"\nCourier '{deleted['name']}' deleted successfully!")
                    
                    # Update any orders that referenced this courier
                    for order in orders:
                        if order['courier'] == courier_idx:
                            order['courier'] = -1
                        elif order['courier'] > courier_idx:
                            order['courier'] -= 1
                else:
                    print("\nInvalid courier number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        else:
            print("Invalid choice. Please try again.")

# Product Functions (updated for WEEK 4)
def print_product_menu():
    print("\n--- Products Menu ---")
    print("0. Return to Main Menu")
    print("1. View Products")
    print("2. Add New Product")
    print("3. Update Product")
    print("4. Delete Product")

def handle_product_menu():
    while True:
        print_product_menu()
        choice = input("\nSelect an option: ")
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n--- Products List ---")
            for idx, product in enumerate(products):
                print(f"{idx}: {product['name']} - £{product['price']:.2f} ({product['type']})")
        elif choice == "2":
            name = input("\nEnter product name: ").strip()
            while not name:
                print("Name cannot be empty")
                name = input("Enter product name: ").strip()
            
            while True:
                try:
                    price = float(input("Enter product price: "))
                    if price <= 0:
                        print("Invalid price!")
                        continue
                    break
                except ValueError:
                    print("Invalid price. Please enter a number")
            
            product_type = input("Enter product type (drink/food): ")
            while product_type not in ['drink', 'food']:
                print("Invalid type. Please enter 'drink' or 'food'")
                product_type = input("Enter product type (drink/food): ")
            
            products.append({
                "name": name,
                "price": price,
                "type": product_type
            })
            print(f"\nProduct '{name}' added successfully!")
        elif choice == "3":
            if not products:
                print("\nNo products available to update")
                continue
            
            print("\n--- Products List ---")
            for idx, product in enumerate(products):
                print(f"{idx}: {product['name']} - £{product['price']:.2f} ({product['type']})")
            
            try:
                product_idx = int(input("\nEnter product number to update: "))
                if 0 <= product_idx < len(products):
                    product = products[product_idx]
                    print("\nLeave blank to keep current value")
                    
                    new_name = input(f"Name [{product['name']}]: ").strip()
                    if new_name:
                        product['name'] = new_name
                    
                    new_price = input(f"Price [{product['price']}]: ").strip()
                    if new_price:
                        try:
                            product['price'] = float(new_price)
                        except ValueError:
                            print("Invalid price - keeping current value")
                    
                    new_type = input(f"Type [{product['type']}]: ").strip()
                    if new_type and new_type in ['drink', 'food']:
                        product['type'] = new_type
                    
                    print("\nProduct updated successfully!")
                else:
                    print("\nInvalid product number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        elif choice == "4":
            if not products:
                print("\nNo products available to delete")
                continue
            
            print("\n--- Products List ---")
            for idx, product in enumerate(products):
                print(f"{idx}: {product['name']} - £{product['price']:.2f} ({product['type']})")
            
            try:
                product_idx = int(input("\nEnter product number to delete: "))
                if 0 <= product_idx < len(products):
                    deleted = products.pop(product_idx)
                    print(f"\nProduct '{deleted['name']}' deleted successfully!")
                else:
                    print("\nInvalid product number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        else:
            print("Invalid choice. Please try again.")

# Main Menu
def employee_menu():
    while True:
        print("\n--- Main Menu ---")
        print("0. Exit")
        print("1. Products Menu")
        print("2. Orders Menu")
        print("3. Couriers Menu")
        
        choice = input("\nSelect an option: ")
        
        if choice == "0":
            save_products()
            save_couriers()
            save_orders()
            print("\nExiting Application, Goodbye!")
            break
        elif choice == "1":
            handle_product_menu()
        elif choice == "2":
            handle_order_menu()
        elif choice == "3":
            handle_courier_menu()
        else:
            print("Invalid choice. Please try again.")

def customer_menu():
    print("\n--- Customer Menu ---")
    print("0. Return to Main Menu")
    print("1. View Menu")
    print("2. View Basket")
    print("3. Complete Order")
    # Implement customer functionality as needed

# Initialize data (will keep defaults if files don't exist)
load_products()
load_couriers()
load_orders()

# Main application loop
while True:
    print("\n--- Login Menu ---")
    print("0. Exit")
    print("1. Customer Menu")
    print("2. Employee Menu")  
    
    login_choice = input("\nSelect an option: ")

    if login_choice == "0":
        save_products()
        save_couriers()
        save_orders()
        print("Exiting Application, Goodbye!")
        break   
    elif login_choice == "1":
        customer_menu()
    elif login_choice == "2":
        employee_menu()
    else:
        print("Invalid choice. Please try again.")
