# # Example: Function Returning a Value

# Let's make our rectangle area function return the area instead of printing it:

def calculate_rectangle_area_return(length, width):
    area = length * width
    return area

# Calling the function and storing the returned value
my_area = calculate_rectangle_area_return(12, 6)
print(f"The calculated area is: {my_area}")

# We can also use the returned value directly
print(f"Another area calculation: {calculate_rectangle_area_return(4, 4)}")