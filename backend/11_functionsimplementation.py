# In this practical exercise, we will write Python functions to perform operations on lists, tuples, dictionaries, and sets. This will solidify your understanding of how to manipulate these structures programmatically and how to choose the right one for specific tasks.

# Objective:

# Write a function that takes a list of numbers and returns a new list containing only the even numbers.
# Write a function that takes a list of strings and returns a tuple containing the longest and shortest strings.
# Write a function that takes a dictionary of student scores and returns the student with the highest score.
# Write a function that takes two lists of numbers and returns a set containing the numbers that appear in both lists (intersection).
# Identify a scenario where using a function to operate on a specific data structure is particularly beneficial.


# --- Function 1: Filter Even Numbers from a List --- 


def filter_even_numbers(numbers_list):
    """Filters a list of numbers and returns a new list containing only even numbers."""
    even_numbers = []
    for number in numbers_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Test Case 1
sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_result = filter_even_numbers(sample_numbers)
print(f"Original numbers: {sample_numbers}")
print(f"Even numbers: {even_result}")

# --- Function 2: Find Longest and Shortest Strings in a List --- 

def find_longest_shortest_strings(string_list):
    """Finds the longest and shortest strings in a list and returns them as a tuple."""
    if not string_list:
        return (None, None) # Handle empty list case

    longest_string = string_list[0]
    shortest_string = string_list[0]

    for s in string_list:
        if len(s) > len(longest_string):
            longest_string = s
        if len(s) < len(shortest_string):
            shortest_string = s
            
    return (longest_string, shortest_string)

# Test Case 2
sample_strings = ["apple", "banana", "kiwi", "strawberry", "grape"]
longest, shortest = find_longest_shortest_strings(sample_strings)
print(f"Sample strings: {sample_strings}")
print(f"Longest string: {longest}")
print(f"Shortest string: {shortest}")

# Test with empty list
print(f"Longest/Shortest in empty list: {find_longest_shortest_strings([])}")

# --- Function 3: Find Student with Highest Score in a Dictionary --- 

def get_top_student(scores_dict):
    """Finds the student with the highest score from a dictionary of scores."""
    if not scores_dict:
        return None # Handle empty dictionary case

    top_student = None
    highest_score = -1 # Assuming scores are non-negative

    for student, score in scores_dict.items():
        if score > highest_score:
            highest_score = score
            top_student = student
            
    return top_student

# Test Case 3
sample_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 92}
top_student_name = get_top_student(sample_scores)
print(f"Student scores: {sample_scores}")
print(f"Top student: {top_student_name}") # Note: If multiple students have the same highest score, this returns the first one encountered.

# Test with empty dictionary
print(f"Top student in empty scores: {get_top_student({})}")

# --- Function 4: Find Common Numbers (Intersection) --- 

def find_common_numbers(list1, list2):
    """Finds the common numbers between two lists using set intersection."""
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

# Test Case 4
numbers_list_a = [1, 2, 3, 4, 5, 6]
numbers_list_b = [4, 5, 6, 7, 8, 9]
common_nums = find_common_numbers(numbers_list_a, numbers_list_b)
print(f"List A: {numbers_list_a}")
print(f"List B: {numbers_list_b}")
print(f"Common numbers: {common_nums}")

# --- Scenario Identification --- 

# 5. Identify a scenario where using a function to operate on a specific data structure is particularly beneficial.

print("--- Scenario Identification ---")
print("Scenario: Calculating the average price of products in an e-commerce inventory.")
print("Data Structure: A list of dictionaries, where each dictionary represents a product and contains a 'price' key.")
print("Benefit of Function: A function can abstract the logic of iterating through the list, accessing the 'price' from each product dictionary, summing them up, and dividing by the count. This makes the code reusable, readable, and less prone to errors.")

# Example of such a function (conceptual):
# def calculate_average_product_price(inventory_list):
#     if not inventory_list:
#         return 0
#     total_price = sum(product['price'] for product in inventory_list)
#     return total_price / len(inventory_list)

# This demonstrates how a function encapsulates complex operations on a data structure.
