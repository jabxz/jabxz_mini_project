# Mini Project - Week 1 (App for managing products)

# Product list 

products =["Americano", "Latte", "Mocha", "Hot Chocolate", "Iced Coffee", "Flat White", "Espresso"] # List[] including the products i want to use on the app
other_products =["Croissant", "Panini", "Muffin", "Toastie", "Brownie", "Choc Chip Cookie"]
# Print Main menu 

print("Main Menu:") # Prints the title of page being -- "Main Menu" --
print("0. Exit")    # Prints an option to exit the app
print("1. Products Menu") # Prints an option to continue to another Menu 

main_choice = input("\nSelect an option: ") # input for the user to interact and choose whether or not they wish to proceed or exit 

if main_choice == "0":     # if statement for the program to read that if the users input is equal to (==) 0(Exit) then the app will then close
    print("Exiting Applicaton, Goodbye!") # Prints a message after the user has chosen to exit 

elif main_choice == "1":   # elif statement for the program to read that if the users input is equal to (==) 1 then the app will then proceed to the menu
     # Products Menu
    print("\nProducts Menu:") # Prints the title of the new page after proceeding -- "Products Menu" --
    

    print("0. Return to Main Menu") # Prints an option to return to main menu
    print("1. View Products")       # Prints an option to view products 
    print("2. Add a new product")   # Prints an option to add a new product
    print("3. Update product list") # Prints an option to update a product
    print("4. Delete a product")    # Prints an option to delete a product    
    product_choice = input("\nSelect an option: ")  # input for the user to interact and select any of the above options from "0-4"

    if product_choice == "0":  # if statement for the program to read that if users input is equal to (==) "0" then the app will then return to the first screen
       print("Returning to main menu...") # Prints a message after the user chooses to return to main menu 

    elif product_choice == "1": # elif statement for the program to read that if users input is equal to (==) "1" then the app will show the list of products 
        # View products 
        print("\nProducts:")    # Prints a header for the list of products (\n is used to tell the program to move to the next line before printing what comes next)
        index = 0               # Initializes the variable "index" to 0. This will be used to number the products.
        for product in products: # Starts a loop that iterates over each item in the "Products" list 
            print(str(index) + ": " + product) # Prints the current index and product name, formatted as "0: product_name". 
            index = index + 1   # Increments the index by 1 


        more_options = input("\nWould you like to see our food menu? (yes/no) ")
        if more_options.lower() == "yes": 
           print("\nShowing food menu...")
           print("\nFood Products:")
           index = 0
           for item in other_products:
              print(str(index) + ": " + item)
              index += 1
        else:
           print("\nOkay!")

        


# Add products 

    elif product_choice == "2": # elif statement for the program to read that if users input is equal to (==) "2" then the app will print the products with a following option to add a product
        
        print("\nProducts:")  
        index = 0
        for product in products:
         print(str(index) + ": " + product)
         index = index + 1 
        
        new_product = input("What would you like to add? ") # Initializes the variable "new_product" to an input for the user to interact and choose a product they would like to add
        products.append(new_product) # the use of the .append is so that users chosen addition will now appear on the end of the original list using the variable "new_product" 
        print("\nYou have added:" + new_product) # Prints a message telling the user what they have added using the variable "new_product"
        
        

# Show updated list  

        print("\nProducts:")  
        index = 0 # Refer to line 34
        for product in products:# Refer to line 35
         print(str(index) + ": " + product) # Refer to line 36
         index = index + 1 # Refer to line 37

# Update Product

    elif product_choice == "3": #elif statement for python to read that if users input is equal to (==) "3" then the app will continue to show an option to update a product
       index = 0 # Refer to line 34
       for product in products: # Refer to line 35
        print(str(index) + ": " + product) #Refer to line 36
        index = index + 1 # Refer to line 37

       update_index = int(input("\nEnter the number of the product you wish to update: ")) # Initializes the variable "update_index" to an input for the user to interact and update a product
       new_name = input("Enter the name of the new product: ") # Initializes the variable "new_name" to an input for the user to change the name of the existing product
       products[update_index] = new_name # Replaces the product name at 'update_index' in the 'products' list with 'new_name'. 
       print("\nProduct Updated") # Prints a message telling the user that products have been update 

# Show updated list
    
       index = 0 # Refer to line 34
       for product in products: # Refer to line 35
        print(str(index) + ": " + product)  #Refer to line 36
        index = index + 1 # Refer to line 37

    elif product_choice == "4":
   # Delete Product
        index = 0 # Refer to line 34
        for product in products: # Refer to line 35
         print(str(index) + ": " + product)  #Refer to line 36
         index = index + 1 # Refer to line 37

        delete_index = int(input("\nEnter the number of the product you wish to delete:")) # Initializes the variable "delete_index" to an input for the user to interact and decide a product they wish to remove
        deleted_product = products.pop(delete_index) # Takes the users input and uses the .pop function to remove a product from the list and uses another variable "deleted_product" to show in the next line what product was deleted when printed
        print("\nYou Deleted " + deleted_product)        # Prints a message showing which product the user decided to delete 

    # Show updated list 
      
        index = 0 # Refer to line 34
        for product in products:  # Refer to line 35
         print(str(index) + ": " + product)  #Refer to line 36
         index = index + 1 # Refer to line 37



 




