# #Problem: We need to store detailed information about a user, including their username, email, age, and a list of their favorite hobbies. We need to be able to easily access any piece of this information by its name.

# Analysis:

# We have distinct pieces of information (username, email, age, hobbies).
# Each piece of information has a clear identifier (its name).
# We need to retrieve specific pieces of information quickly using these identifiers.
# The user's profile information might be updated (e.g., age changes).
# Best Data Structure: Dictionary

# A dictionary is the perfect fit because: 

# 1. It allows us to store key-value pairs, where the key is the name of the information (e.g., "username") and the value is the actual data (e.g., "john_doe").
# 2. It provides O(1) average time complexity for lookups, making it efficient to access any piece of information by its name.      

user_profile = {
    "user_id": "u12345",
    "username": "coder_gal",
    "email": "coder.gal@example.com",
    "age": 28,
    "is_premium": False,
    "hobbies": ["coding", "reading", "hiking"]
}

# Accessing information
print(f"Username: {user_profile['username']}")
print(f"Email: {user_profile.get('email')}")
print(f"Age: {user_profile['age']}")
print(f"Hobbies: {user_profile['hobbies']}")

# Updating information
user_profile["age"] = 29
user_profile["hobbies"].append("photography") # Modifying the list value
user_profile["last_login"] = "2023-10-27 10:00:00"

print(f"Updated Age: {user_profile['age']}")
print(f"Updated Hobbies: {user_profile['hobbies']}")
print(f"Last Login: {user_profile['last_login']}")