# Multiple Return Values

# Python functions can return multiple values by returning them as a tuple. When you receive the return value, you can unpack it into multiple variables.

def get_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Calling the function and unpacking the returned tuple
rect_area, rect_perimeter = get_rectangle_properties(8, 4)

print(f"Area: {rect_area}")
print(f"Perimeter: {rect_perimeter}")

