# Data structures
products = ["Americano", "Latte", "Mocha", "Hot Chocolate", "Iced Coffee", "Flat White", "Espresso"]
other_products = ["Croissant", "Panini", "Muffin", "Toastie", "Brownie", "Choc Chip Cookie"] 
orders = []
order_status_options = ["PREPARING", "DISPATCHED", "OUT FOR DELIVERY", "DELIVERED"]
couriers = ["Deliveroo", "Just Eat", "Uber Eats", "Costa Coffee", "Starbucks", "Pret-A-Manger", "Greggs"]

# File names 
products_file = "products.txt"
couriers_file = "couriers.txt"


def print_order_menu():
    print("\n--- Order Menu ---")
    print("0. Return to Main Menu")
    print("1. View All Orders")
    print("2. Add New Order")
    print("3. Update Order Status")
    print("4. Update Order Info")
    print("5. Delete Order")

def print_courier_menu():
    print("\n--- Courier Menu ---")
    print("0. Return to Main Menu")
    print("1. View All Couriers")
    print("2. Add New Courier")
    print("3. Update Courier")
    print("4. Delete Courier")

def customer_menu():
    print("\n--- Customer Menu ---")
    print("0. Return to Main Menu")
    print("1. View Menu")
    print("2. View Basket")
    print("3. Complete Order")

def print_orders():
    if not orders:
        print("\nNo orders found.")
    else:
        print("\n--- Current Orders ---")
        for idx, order in enumerate(orders):
            courier_idx = order.get("courier", -1)
            courier_name = couriers[courier_idx] if 0 <= courier_idx < len(couriers) else "Unknown"
            print(f"{idx}: Name: {order.get('customer_name', 'Unknown')} | " 
                  f"Address: {order.get('customer_address', 'Unknown')} | "
                  f"Phone: {order.get('customer_phone', 'Unknown')} | "
                  f"Courier: {courier_name} | "
                  f"Status: {order.get('status', 'Unknown')}")
def add_order():
    name = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")
    phone = input("Enter Customer Phone Number: ")
    
    # Show available couriers
    print("\nAvailable Couriers:")
    for idx, courier in enumerate(couriers):
        print(f"{idx}: {courier}")
    
    try:
        courier_idx = int(input("\nEnter the number of the courier: "))
        if 0 <= courier_idx < len(couriers):
            new_order = {
                'customer_name': name,
                'customer_address': address,
                'customer_phone': phone,
                'courier': courier_idx,
                'status': "PREPARING"
            }
            orders.append(new_order)
            print("\nOrder added successfully!")
        else:
            print("\nInvalid courier selection!")
    except ValueError:
        print("\nPlease enter a valid number!")
        return

def update_order_status():
    if not orders:
        print("\nNo Orders To Update")
        return
    
    print("\n--- Existing Orders ---")
    print_orders()

    try:
        order_index = int(input("\nEnter the number of the order you wish to update: "))
        if order_index < 0 or order_index >= len(orders):
            print("\nOrder does not exist!")
            return
    except ValueError:
        print("\nPlease Try again!")
        return

    print("\n---Status Options ---")
    for idx, status in enumerate(order_status_options):
        print(f"{idx}: {status}")
    
    try:
        status_index = int(input("\nEnter the number of the updated status: "))
        if status_index < 0 or status_index >= len(order_status_options):
            print("\nStatus does not exist!")
            return
    except ValueError:
        print("\nPlease Try Again!")
        return
    
    orders[order_index]["status"] = order_status_options[status_index]
    print("\nStatus Updated!")

def update_order_details():
    if not orders:
        print("\nNo Orders Available!")
        return
    
    print("\n--- Order Info ---")
    print_orders()

    try:
        order_index = int(input("\nEnter the number of the order you wish to update: "))
        if order_index < 0 or order_index >= len(orders):
            print("Order doesn't exist!")
            return
    except ValueError:
        print("\nPlease Try Again!")
        return

    order = orders[order_index]

    print("\nLeave blank if you wish to keep detail the same")
    for key in order:
            current_value = order[key]
            new_value = input(f"{key} [{current_value}]: ").strip()
            if new_value:
                order[key] = new_value

    print("\nOrder Successfully Updated!")

def delete_order():
    if not orders:
        print("\nNo Orders To Delete!")
        return
    
    print("\n--- Available Orders ---")
    print_orders()

    try:
        order_index = int(input("\nEnter the number of the order you wish to delete: "))
        if order_index < 0 or order_index >= len(orders):
            print("Order Does Not Exist!")
            return
    except ValueError:
        print("\nPlease Try Again!")
        return

    deleted_order = orders.pop(order_index)
    print("\nOrder Successfully Deleted!")

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
            
def handle_courier_menu():
    while True:
        print_courier_menu()
        choice = input("\nSelect an option: ")
        
        if choice == "0":
            break
        elif choice == "1":
            print("\n--- Couriers List ---")
            for idx, courier in enumerate(couriers):
                print(f"{idx}: {courier}")
        elif choice == "2":
            new_courier = input("\nEnter new courier name: ").strip()
            if new_courier:
                couriers.append(new_courier)
                print(f"\nCourier '{new_courier}' added successfully!")
        elif choice == "3":
            print("\n--- Update Courier ---")
            for idx, courier in enumerate(couriers):
                print(f"{idx}: {courier}")
            
            try:
                courier_idx = int(input("\nEnter courier number to update: "))
                if 0 <= courier_idx < len(couriers):
                    new_name = input("Enter new courier name: ").strip()
                    if new_name:
                        couriers[courier_idx] = new_name
                        print("\nCourier updated successfully!")
                    else:
                        print("\nNo changes made.")
                else:
                    print("\nInvalid courier number!")
            except ValueError:
                print("\nPlease enter a valid number!")
        elif choice == "4":
            print("\n--- Delete Courier ---")
            for idx, courier in enumerate(couriers):
                print(f"{idx}: {courier}")
            
            try:
                courier_idx = int(input("\nEnter courier number to delete: "))
                if 0 <= courier_idx < len(couriers):
                    deleted = couriers.pop(courier_idx)
                    print(f"\nCourier '{deleted}' deleted successfully!")
                                   
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

def handle_customer_menu():
    while True:
        customer_menu()
        customer_choice = input("\nSelect an option: ")

        if customer_choice == "0":
            break 
        elif customer_choice == "1":
           print_menu()
       # elif customer_choice == "2":
          #  print_basket()
      #  elif customer_choice == "3":
           # complete_order()
       # else:
            #print("Invalid choice, please try again!")
        


def employee_menu():
# Main program loop
    while True:
    # Print Main menu
        print("\n--- Main Menu--- ")
        print("0. Exit")
        print("1. Products Menu")
        print("2. Orders Menu")
        print("3. Couriers Menu")
        
        main_choice = input("\nSelect an option: ")
        
        if main_choice == "0":
            print("\nExiting Application, Goodbye!")
            break
        elif main_choice == "1":
            # Products Menu
            while True:
                print("\n--- Products Menu ---")
                print("0. Return to Main Menu")
                print("1. View Products")
                print("2. Add a new product")
                print("3. Update product list")
                print("4. Delete a product")
                
                product_choice = input("\nSelect an option: ")
                
                if product_choice == "0":
                    break
                elif product_choice == "1":
                    
                    while True:
                        print("\nFood and Drinks Menu:")
                        print("1. Drinks Menu")
                        print("2. Food Menu")
                        print("0. Return to products menu")

                        menu_choice = input("\n What menu would you like to see? ")

                        if menu_choice == "0":
                            print("\nReturning to products menu...")
                            break
                        
                        elif menu_choice == "1":
                            print("\nDrinks Menu:")
                            for index, product in enumerate(products):
                                print(f"{index}: {product}")
                            
                        
                        elif menu_choice == "2":
                            print("\nFood Menu:")
                            for index, item in enumerate(other_products):
                                print(f"{index}: {item}")
                            
                            

                elif product_choice == "2":
                    while True:
                        print("\nAdd Product Menu:")
                        print("1. Add a drink")
                        print("2. Add a food item")
                        print("0. Exit")
            
                        add_choice = input("\nWhat would you like to add? (1 for drinks, 2 for food, 0 to cancel): ")
            
                        if add_choice == "0":
                            print("\nReturning to Products Menu...")
                            break
                
                        elif add_choice == "1":
                            # Add drink
                            print("\nCurrent Drink Menu:")
                            for index, product in enumerate(products):
                                print(f"{index}: {product}")
                            
                            new_product = input("\nEnter the new drink to add (or press Enter to cancel): ")
                            if new_product.strip() == "":
                                print("\nDrink addition cancelled.")
                                continue
                                
                            products.append(new_product)
                            print(f"\nYou have added: {new_product} to drinks")
                            
                            print("\nUpdated Drink Menu:")
                            for index, product in enumerate(products):
                                print(f"{index}: {product}") 
                            break
                
                        elif add_choice == "2":
                        # Add food item
                            print("\nCurrent Food Menu:")
                            for index, item in enumerate(other_products):
                                print(f"{index}: {item}")
                        
                        new_item = input("\nEnter the new food item to add (or press Enter to cancel): ")
                        if new_item.strip() == "":
                            print("\nFood addition cancelled.")
                            continue
                            
                        other_products.append(new_item)
                        print(f"\nYou have added: {new_item} to food menu")
                        
                        print("\nUpdated Food Menu:")
                        for index, item in enumerate(other_products):
                            print(f"{index}: {item}")
                        break
                
                elif product_choice == "3":
                            while True:
                                print("\nUpdate Product Menu:")
                                print("1. Update Drink Menu")
                                print("2. Update Food Menu")
                                print("0. Exit")

                                update_choice = input("\nWhat menu would you like to update? ")

                                if update_choice == "0":
                                    print("\nReturning to Products Menu...")
                                    break 
                                
                                elif update_choice == "1":
                                    print("\nCurrent Drinks Menu:")
                                    for index, product in enumerate(products):
                                        print(f"{index}: {product}")

                                    try:
                                        
                                        
                                        update_drink = int(input("\nEnter the number of the product you wish to update: "))
                                        new_drink = input("Enter the name of the new product: ")
                                        products[update_drink] = new_drink
                                        print("\nProduct Updated!")
                                        
                                        print("\nUpdated Products:")
                                        for index, product in enumerate(products):
                                            print(f"{index}: {product}")
                                    except(ValueError, IndexError):
                                        print("\nInvalid input or product number!")
                                
                                elif update_choice == "2":
                                    print("\nCurrent Food Menu:")
                                    for index, item in enumerate(other_products):
                                        print(f"{index}: {item}")

                                    try:
                                        update_food = int(input("\nEnter the number of the product you wish to update: "))
                                        new_food = input("Enter the name of the new product: ")
                                        other_products[update_food] = new_food 
                                        print("\nProduct Updated!")

                                        print("\nUpdated Products:")
                                        for index, item in enumerate(other_products):
                                            print(f"{index}: {item}")
                                    except(ValueError, IndexError):
                                        print("\nInvalid input or product number!")
                        
                elif product_choice == "4":
                            # Delete product
                            print("\nProducts:")
                            for index, product in enumerate(products):
                                print(f"{index}: {product}")
                            
                            try:
                                delete_index = int(input("\nEnter the number of the product you wish to delete: "))
                                deleted_product = products.pop(delete_index)
                                print(f"\nYou Deleted {deleted_product}")
                                
                                print("\nUpdated Products:")
                                for index, product in enumerate(products):
                                    print(f"{index}: {product}")
                            except (ValueError, IndexError):
                                print("\nInvalid input or product number!")

        elif main_choice == "2":
            handle_order_menu ()    

        elif main_choice == "3":
            handle_courier_menu()

while True:
    print("\n--- Login Menu ---")
    print("0. Exit")
    print("1. Customer Menu")
    print("2. Employee Menu ")  
    
    login_choice = input("\nSelect an option: ")

    if login_choice == "0":
        print("Exiting Application, Goodbye!")
        break   
    elif login_choice == "1":
        customer_menu()
    elif login_choice == "2":
        employee_menu()
    else:
        print("Invalid choice. Please try again.")

        def print_menu():
            while True: 
                print("\nFood and Drinks Menu:")
                print("1. Drinks Menu")
                print("2. Food Menu")
                print("0. Return to products menu")

                menu_choice = input("\n What menu would you like to see")

                if menu_choice == "0":
                    print("\nReturning to products menu")
                    break 

                elif menu_choice =="1":
                    print("\n--- Drinks Menu ---")
                    for index, product in enumerate(products):
                        print(f"{index}: {product}")

                elif menu_choice == "2":
                    print("\n--- Food Menu ---")
                    for index, item in enumerate(other_products):
                        print(f"{index}: {item}")