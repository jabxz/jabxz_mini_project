# Keiron-Portfolio

# Project Background 

This project is a CLI-based order management system designed to manage a pop-up café's products, couriers, and orders. It provides full CRUD (Create, Read, Update, Delete) functionality and persists all data in a PostgreSQL database.

# Features

- **Products Management**
  - View all products
  - Add new products (name, price, type)
  - Update existing products
  - Delete products

- **Couriers Management**
  - View all couriers
  - Add new couriers (name, last name, company, phone)
  - Update courier details
  - Delete couriers

- **Orders Management**
  - View all orders with customer details
  - Create new orders with customer info and product selection
  - Update order status
  - Delete orders

## Technology Stack

- Python 3
- PostgreSQL database
- psycopg2 database adapter
- Environment variables for secure configuration

# Client requirements 

- Maintain a list of drink and food products 
- Maintain a list of couriers 
- Create, read, update, and delete orders
- Allow order status updates 
- Persist all data so that it is not lost when the app is closed and reloaded 
- Receive regular software updates. 

# How to run the app ?
Prerequisites
- Python 3.8 or later installed

- PostgreSQL database server running

- Required Python packages: psycopg2-binary and python-dotenv

Set up your environment:

(windows)
pip install psycopg2-binary python-dotenv

Configure your database:

Create a .env file in the project directory with your PostgreSQL credentials:

text
POSTGRES_HOST=your_database_host
POSTGRES_DB=your_database_name
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password

Run the application:

python app.py

Using the Application
Navigate through the intuitive menu system using number inputs

All changes are immediately persisted to your PostgreSQL database

The main menu offers access to three subsystems:

- Products management (add, view, update, delete)

- Couriers management (add, view, update, delete)

- Orders management (create, view, update status, delete)

Troubleshooting
If you encounter connection issues, verify your .env credentials

Ensure your PostgreSQL server is running and accessible

Check that all required tables exist in your database


# How to run any unit test ? 

To run unit tests, you will need to have pytest installed. Simply navigate to your project directory in the terminal and run the command pytest -v to execute all tests with detailed output.


# Project reflections 

# How my design meets the project requirements ?

I designed this application with a modular architecture that cleanly separates concerns between:

- Database operations (CRUD functions for products, couriers, and orders)

- User interface (menu navigation and input handling)

- Business logic (order processing and status management)

The PostgreSQL backend ensures data persistence between sessions, while the clear menu hierarchy makes all required functionality easily accessible. Each component was built to specifically address one of the client requirements, from product management to order status updates.

# How I guaranteed the projects requirments ? 

I implemented a multi-layered verification approach:

- Functional Testing: Manually exercised every menu option to confirm CRUD operations worked as intended

- Database Validation: Verified data integrity by checking PostgreSQL records after each operation

- Edge Case Testing: Tested with invalid inputs, empty values, and extreme cases to ensure robustness

- User Flow Verification: Walked through complete order lifecycle from creation to status updates

The combination of manual testing and direct database inspection provided comprehensive validation that all requirements were properly implemented and integrated.

# If i had more time what is one thing i would improve upon? 

If I had more time, I would focus on implementing proper unit testing throughout the application. While I understand the importance of testing, I didn't quite reach the point where I could begin integrating pytest and writing comprehensive test cases for all the database operations and menu functions. This would have helped verify each component works correctly in isolation before combining them in the full application.

# What i enjoyed implementing most ? 

The database integration and seeing how all the CRUD operations work together to create a fully functional system is what I would say i enjoyed most. The PostgreSQL implementation provided a great learning experience in database management.