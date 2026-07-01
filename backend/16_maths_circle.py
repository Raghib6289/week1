# Hands-on Component: Function with Parameters and Return Value

# Let's enhance our previous function. This time, we want a function that calculates the circumference and area of a circle, given its radius, and returns both values.

# Step 1: Import the math module to get the value of pi.

# Step 2: Define a function named calculate_circle_properties that accepts one parameter: radius.

# Step 3: Inside the function, calculate the area using the formula: area = math.pi * (radius ** 2).

# Step 4: Calculate the circumference using the formula: circumference = 2 * math.pi * radius.

# Step 5: Return both area and circumference.

# Step 6: Call the function with a radius (e.g., 5) and store the returned values in two variables, circle_area and circle_circumference.

# Step 7: Print the calculated area and circumference.

import math

# Step 2-5: Define the function
def calculate_circle_properties(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return area, circumference

# Step 6: Call the function and unpack values
circle_area, circle_circumference = calculate_circle_properties(5)

# Step 7: Print the results
print(f"For a circle with radius 5")
print(f"Area: {circle_area:.2f}") # Using .2f for formatting to 2 decimal places
print(f"Circumference: {circle_circumference:.2f}")