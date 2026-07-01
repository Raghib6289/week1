
# Lambda functions, also known as anonymous functions, are small, single-expression functions that are defined without a name using the lambda keyword. They are often used when you need a simple function for a short period of time, typically as an argument to higher-order functions (functions that take other functions as arguments).

# Why Use Lambda Functions?

# Lambda functions are useful for:

# Conciseness: They allow you to write small functions in a single line, making your code more compact when appropriate.
# Readability (in specific contexts): When used with functions like map(), filter(), or sorted(), a lambda function can make the intent clearer than defining a separate named function.
# Avoiding Namespace Pollution: Since they are anonymous, they do not add names to your program's namespace, which can be beneficial in certain situations.

add_ten = lambda x: x + 10

print(add_ten(5))   # Output: 15
print(add_ten(20))  # Output: 30


multiply = lambda x, y: x * y

print(multiply(4, 6)) # Output: 24
print(multiply(10, 2)) # Output: 20


# 1. map(): Applying a function to each item in an iterable.

# map(function, iterable) applies function to every item of iterable and returns a map object (which can be converted to a list).

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# 2. filter(): Filtering items from an iterable based on a condition.

# filter(function, iterable) constructs an iterator from elements of iterable for which function returns true.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4, 6, 8, 10]


# 3. sorted(): Sorting lists based on a custom key.

# The key argument in sorted() expects a function that returns a value to sort by.

# List of tuples (name, age)
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# Sort by age
sorted_by_age = sorted(people, key=lambda person: person[1])
print(sorted_by_age) # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]

# Sort by name
sorted_by_name = sorted(people, key=lambda person: person[0])
print(sorted_by_name) # Output: [('Alice', 30), ('Bob', 25), ('Charlie', 35)]


# Real-World Scenario: Data Processing Pipelines

# In data science or backend processing, you might have a pipeline where you need to perform a series of transformations on data. Lambda functions can be very handy here:

data = [10, -5, 20, 0, -15, 30]

# 1. Filter out negative numbers
positive_data = list(filter(lambda x: x >= 0, data))

# 2. Square the positive numbers
squared_positive_data = list(map(lambda x: x**2, positive_data))

# 3. Sort the squared numbers
sorted_squared_positive_data = sorted(squared_positive_data)

print(f"Original data: {data}")
print(f"Processed data: {sorted_squared_positive_data}")




# ###############important note####################
# Hands-on Component: Using Lambda Functions

# Let's practice using lambda functions with a list of dictionaries representing products.

# Step 1: Create a list of dictionaries, where each dictionary represents a product with keys like 'name', 'price', and 'stock'.

# Step 2: Use the sorted() function with a lambda function as the key to sort the list of products by their 'price' in ascending order.

# Step 3: Use the filter() function with a lambda function to create a new list containing only products that are in stock ('stock' > 0).

# Step 4: Use the map() function with a lambda function to create a list of just the names of the products that are in stock.


# Step 1: Create a list of product dictionaries
products = [
    {'name': 'Laptop', 'price': 1200, 'stock': 15},
    {'name': 'Mouse', 'price': 25, 'stock': 50},
    {'name': 'Keyboard', 'price': 75, 'stock': 0},
    {'name': 'Monitor', 'price': 300, 'stock': 10},
    {'name': 'Webcam', 'price': 50, 'stock': 25}
]

print("Original Products:")
for p in products:
    print(p)

# Step 2: Sort products by price using lambda
sorted_by_price = sorted(products, key=lambda product: product['price'])

print("Products sorted by price:")
for p in sorted_by_price:
    print(p)

# Step 3: Filter products that are in stock using lambda
products_in_stock = list(filter(lambda product: product['stock'] > 0, products))

print("Products currently in stock:")
for p in products_in_stock:
    print(p)

# Step 4: Get names of products in stock using map and lambda
product_names_in_stock = list(map(lambda product: product['name'], products_in_stock))

print("Names of products in stock:")
print(product_names_in_stock)