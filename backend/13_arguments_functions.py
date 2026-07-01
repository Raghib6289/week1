# Keyword Arguments Example:

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

# Calling with positional arguments ,Here order matters
describe_pet("dog", "Buddy")

# Calling with keyword arguments (order does not matter)
describe_pet(pet_name="Lucy", animal_type="cat")


# Default Arguments Example:

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling with only required argument
greet_user("Alice")

# Calling with both arguments
greet_user("Bob", "Good morning")