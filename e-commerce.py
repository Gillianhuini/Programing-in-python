"""You are tasked with developing a Python program for a small e-commerce platform. The program should 
include various functions to perform essential operations related to product management. Design and 
implement the following functions:
1.add_product: This function should take the following parameters:
•product_name (string): representing the name of the product.
•price (float): representing the price of the product.
•quantity (int): representing the initial quantity of the product in stock.
The function should create a dictionary object for the product with the given parameters and return it.
Exercise 2.update_price: This function should take the following parameters:
•product (dictionary): representing the product dictionary object.
•new_price (float): representing the updated price of the product.
The function should update the price of the product in the dictionary and return the modified dictionary.
3.update_quantity: This function should take the following parameters:
•product (dictionary): representing the product dictionary object.
•quantity_change (int): representing the change in quantity of the product (positive for addition, 
negative for subtraction).
The function should update the quantity of the product in the dictionary and return the modified dictionary"""
# Function to add a product
def add_product(product_name, price, quantity):
    return {
        "name": product_name,
        "price": price,
        "quantity": quantity
    }

# Function to update the price of a product
def update_price(product, new_price):
    product["price"] = new_price
    return product

# Function to update the quantity of a product
def update_quantity(product, quantity_change):
    product["quantity"] += quantity_change  # Increase or decrease quantity
    return product
