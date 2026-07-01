# Empty set
empty_set = set()

# Set of integers
numbers_set = {1, 2, 3, 4, 5}

# Set of strings
colors_set = {"red", "green", "blue"}

# Set with duplicates (duplicates are automatically removed)
set_with_duplicates = {1, 2, 2, 3, 3, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}

# Creating a set from a list
my_list = [1, 2, 2, 3, 4, 4, 5]
list_to_set = set(my_list)
print(list_to_set) # Output: {1, 2, 3, 4, 5}

# Creating a set from a string (each character becomes an element)
string_set = set("hello")
print(string_set) # Output: {'h', 'e', 'l', 'o'} (order may vary)