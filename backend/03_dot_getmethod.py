user_profile = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "age": 30
}

print(user_profile.get("username")) # Output: johndoe
print(user_profile.get("city"))      # Output: None (key not found, returns None by default)
print(user_profile.get("city", "Unknown")) # Output: Unknown (key not found, returns specified default value)