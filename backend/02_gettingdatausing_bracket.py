user_profile = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "age": 30
}

print(user_profile["username"]) # Output: johndoe
print(user_profile["age"])      # Output: 30

# Accessing a nested value
student = {
    "name": "Alice",
    "details": {
        "major": "Computer Science",
        "gpa": 3.8
    }
}
print(student["details"]["major"]) # Output: Computer Science

# Attempting to access a non-existent key will raise a KeyError:
# print(user_profile["city"]) # This would cause a KeyError