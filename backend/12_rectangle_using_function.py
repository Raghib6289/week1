# Let's create a simple function to calculate the area of a rectangle. For now, we'll hardcode the dimensions inside the function.

# Step 1: Open your Python IDE or a text editor.

# Step 2: Define a function named calculate_rectangle_area.

# Step 3: Inside the function, define two variables, length and width, and assign them some values (e.g., length = 10, width = 5).

# Step 4: Calculate the area: area = length * width.

# Step 5: Print the result in a user-friendly format, like print(f"The area of the rectangle is: {area}").

# Step 6: Call the function to see the output.

# def calculate_rectangle_area():
#     length = int(input("Enter the length of the rectangle: "))
#     width = int(input("Enter the width of the rectangle: "))
#     area = length * width
#     print(f"The area of the rectangle is: {area}")

# calculate_rectangle_area()




# Let's modify our rectangle area calculation to accept length and width as arguments:


def calculate_rectangle_area(length, width):
    area = length * width
    print(f"The area of a rectangle with length {length} and width {width} is: {area}")

# Calling the function with arguments
calculate_rectangle_area(10, 5)  # length=10, width=5
calculate_rectangle_area(7, 3)   # length=7, width=3


