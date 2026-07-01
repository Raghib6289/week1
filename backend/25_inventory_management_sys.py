# Practical Application: Building a Simple Inventory Management System
# Now that we've explored the core concepts of Object-Oriented Programming – classes, objects, attributes, methods, __init__, inheritance, polymorphism, and encapsulation – it's time to put them into practice. We will build a simplified inventory management system for a small online store. This exercise will reinforce how these OOP principles work together to create a structured and functional application.

# Scenario: Online Store Inventory
# Our online store needs to keep track of its products. Each product has a unique ID, a name, a price, and a quantity in stock. We want to be able to add new products, update their quantities, and display the inventory.

# Designing the Classes
# We can start with a base class for a generic Product and then potentially create subclasses for different types of products if needed (though for this simple example, a single Product class will suffice). We'll focus on demonstrating the OOP concepts.

# Step 1: Define the `Product` Class
# This class will represent a single item in our inventory. It will have attributes for its properties and methods for managing its quantity.

class Product:
    def __init__(self, product_id, name, price, quantity_in_stock=0):
        # Using name mangling for attributes that should be managed internally
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity_in_stock = quantity_in_stock
        print(f"Product '{self.__name}' (ID: {self.__product_id}) created. Initial stock: {self.__quantity_in_stock}")

    # --- Getters for accessing product information --- 
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity_in_stock

    # --- Methods to manage stock --- 
    def add_stock(self, quantity):
        if quantity > 0:
            self.__quantity_in_stock += quantity
            print(f"Added {quantity} units of '{self.__name}'. New stock: {self.__quantity_in_stock}")
        else:
            print("Quantity to add must be positive.")

    def remove_stock(self, quantity):
        if quantity > 0:
            if self.__quantity_in_stock >= quantity:
                self.__quantity_in_stock -= quantity
                print(f"Removed {quantity} units of '{self.__name}'. New stock: {self.__quantity_in_stock}")
                return True # Indicate successful removal
            else:
                print(f"Insufficient stock for '{self.__name}'. Available: {self.__quantity_in_stock}, Requested: {quantity}")
                return False # Indicate failure
        else:
            print("Quantity to remove must be positive.")
            return False

    # --- Method to display product details --- 
    def display_details(self):
        return f"ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price:.2f}, Stock: {self.__quantity_in_stock}"

    # --- Representation for printing the object directly --- 
    def __str__(self):
        return self.display_details()
    
# Step 2: Create an Inventory Class

class Inventory:
    def __init__(self):
        self.products = {}
        print("Inventory system initialized.")

    # Method to add a new product to the inventory
    def add_product(self, product):
        if isinstance(product, Product):
            if product.get_product_id() not in self.products:
                self.products[product.get_product_id()] = product
                print(f"Added '{product.get_name()}' to inventory.")
            else:
                print(f"Product with ID {product.get_product_id()} already exists. Use update_stock() to modify quantity.")
        else:
            print("Invalid product object provided.")

    # Method to get a product by its ID
    def get_product_by_id(self, product_id):
        return self.products.get(product_id)

    # Method to update stock for an existing product
    def update_stock(self, product_id, quantity_change):
        product = self.get_product_by_id(product_id)
        if product:
            if quantity_change > 0:
                product.add_stock(quantity_change)
            elif quantity_change < 0:
                # We need to remove the absolute value of quantity_change
                product.remove_stock(abs(quantity_change))
            else:
                print("Quantity change must be non-zero.")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    # Method to display all products in the inventory
    def display_inventory(self):
        print("--- Current Inventory ---")
        if not self.products:
            print("Inventory is empty.")
            return
        for product_id, product in self.products.items():
            print(product.display_details())
        print("-------------------------")

# Step 3: Demonstrate the Inventory Management System

# Step 3: Using the Inventory System
# Let's create instances and simulate some inventory operations.

# Create an inventory instance
store_inventory = Inventory()

# Create some product instances
laptop = Product("LAP001", "Gaming Laptop", 1200.00, 10)
mouse = Product("MOU002", "Wireless Mouse", 25.50, 50)
keyboard = Product("KEY003", "Mechanical Keyboard", 75.00, 20)

# Add products to the inventory
store_inventory.add_product(laptop)
store_inventory.add_product(mouse)
store_inventory.add_product(keyboard)

# Display the initial inventory
store_inventory.display_inventory()

# Update stock levels
print("--- Updating Stock ---")
store_inventory.update_stock("LAP001", -3) # Sell 3 laptops
store_inventory.update_stock("MOU002", 15) # Receive 15 new mice
store_inventory.update_stock("KEY003", -25) # Try to sell more keyboards than available
store_inventory.update_stock("CAM004", 5) # Try to update stock for a non-existent product

# Display the inventory after updates
store_inventory.display_inventory()

# Get and print details of a specific product
print("--- Getting Specific Product ---")
retrieved_mouse = store_inventory.get_product_by_id("MOU002")
if retrieved_mouse:
    print(f"Details for MOU002: {retrieved_mouse}") # Uses the __str__ method
else:
    print("Mouse not found.")

# Trying to add a duplicate product ID
print("--- Attempting Duplicate Product Add ---")
new_laptop = Product("LAP001", "Budget Laptop", 800.00, 5) # Same ID as Gaming Laptop
store_inventory.add_product(new_laptop)