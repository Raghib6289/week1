# Problem: An application needs to load configuration settings from a file or a database. These settings might include database credentials, API keys, feature flags, and logging levels. The structure of these settings can be hierarchical.

# Analysis:

# Configuration settings are typically named (e.g., DATABASE_URL, API_KEY).
# The structure can be nested (e.g., database settings might have host, port, username, password).
# We need to access these settings easily by their names.
# Settings are generally fixed during application runtime but might be loaded from external sources.
# Best Data Structure: Nested Dictionaries

# Nested dictionaries are ideal for representing configuration settings:

# Hierarchical Structure: Dictionaries can contain other dictionaries, allowing for a natural representation of nested configurations.
# Named Access: Settings are accessed by their names (keys).
# Readability: The structure closely mirrors how configurations are often defined in files (like JSON or YAML).

app_config = {
    "database": {
        "type": "postgresql",
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secure_password123"
    },
    "api": {
        "base_url": "https://api.example.com/v1",
        "timeout_seconds": 30
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/app.log"
    },
    "feature_flags": {
        "new_dashboard": None,
        "email_notifications": False
    }
}

# Accessing settings
db_host = app_config["database"]["host"]
api_timeout = app_config["api"]["timeout_seconds"]
log_level = app_config["logging"]["level"]

print(f"Database Host: {db_host}")
print(f"API Timeout: {api_timeout} seconds")
print(f"Logging Level: {log_level}")

# Checking a feature flag
if app_config["feature_flags"]["new_dashboard"]:
    print("New dashboard feature is enabled!")
else:
    print("New dashboard feature is disabled.")