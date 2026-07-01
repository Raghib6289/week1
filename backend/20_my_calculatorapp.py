# #############ANOTHER EXAMPLES##############

# Hands-on Component: Create a Custom Module for Calculations

# Let's create a simple module for basic arithmetic operations.

# Step 1: Create a new Python file named calculator_ops.py.

# Step 2: Inside calculator_ops.py, define the following functions:

# add(a, b): Returns the sum of a and b.
# subtract(a, b): Returns the result of a - b.
# multiply(a, b): Returns the product of a and b.
# divide(a, b): Returns the result of a / b. Include error handling for division by zero (return an informative string or None if b is 0).
# Step 3: Add docstrings to the module and each function.

# Step 4: Create another Python file named my_calculator.py in the same directory.

# Step 5: In my_calculator.py, import the calculator_ops module.

# Step 6: Call each of the functions from calculator_ops with sample numbers and print the results. Make sure to test the division by zero case.


# calculator_ops.py

"""A simple module for basic calculator operations."""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers (a - b)."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the result of a divided by b. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Optional: Add a test block
if __name__ == "__main__":
    print("Testing calculator_ops module...")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")






#     ##after creation of local import pakage 
#     ##now we can call it another python file withiin same folder or directory
#     ##example
#     # my_calculator.py

# # Step 5: Import the custom module
# import calculator_ops

# # Step 6: Call functions and print results
# num1 = 25
# num2 = 5
# num3 = 0

# print(f"--- Performing Calculations ---")

# # Addition
# sum_result = calculator_ops.add(num1, num2)
# print(f"{num1} + {num2} = {sum_result}")

# # Subtraction
# diff_result = calculator_ops.subtract(num1, num2)
# print(f"{num1} - {num2} = {diff_result}")

# # Multiplication
# prod_result = calculator_ops.multiply(num1, num2)
# print(f"{num1} * {num2} = {prod_result}")

# # Division (normal case)
# div_result =calculator_ops.divide(num1, num2)
# print(f"{num1} / {num2} = {div_result}")

# # Division (by zero case)
# div_by_zero_result =calculator_ops.divide(num1, num3)
# print(f"{num1} / {num3} = {div_by_zero_result}")

# # You can also import specific functions if preferred:
# # from calculator_ops import add, subtract
# # print(f"Using imported add: {add(100, 200)}")