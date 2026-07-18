# Creating Your Own Simple Python Module: Organizing Your Code
# Now that you understand how to import and use existing modules, let's explore how to create your own. Creating custom modules is a fundamental practice for building larger, more organized Python applications. It allows you to encapsulate related functionality and reuse it across different parts of your project or even in entirely different projects.

# What is a Custom Module?

# A custom module in Python is simply a file containing Python code. This file can define functions, classes, variables, or any other Python constructs. When you create a Python file (e.g., my_module.py), you can then import it into another Python script just like you would import a standard library module.

# Steps to Create and Use a Custom Module

# Let's walk through the process with a practical example. We'll create a module for performing some basic string manipulation tasks.



import random
import math # Included for potential future use, not strictly needed for current task


# Step 3: Define Helper Functions

# Let's define a function to generate our raw sensor data. This function will simulate readings, including some potentially invalid ones.

def generate_raw_readings(num_readings=20, max_value=100):
    """Generates a list of simulated sensor readings, including potential invalid entries."""
    readings = []
    for _ in range(num_readings):
        # Simulate some valid readings
        if random.random() > 0.1: # 90% chance of a valid reading
            reading = random.uniform(0, max_value)
            readings.append(reading)
        else:
            # Simulate an invalid reading (e.g., None or a negative number)
            if random.random() > 0.5:
                readings.append(None)
            else:
                readings.append(random.uniform(-50, -1)) # Negative value
    return readings

# Step 4: Define the Core Processing Logic Function

# This function will take the raw readings, clean them, process them, and return the final aggregate. We'll use lambda functions here.

def process_sensor_data(raw_data):
    """Processes raw sensor data: filters invalid entries, squares valid ones, and sums them."""
    
    # 1. Filter out invalid readings (None or negative values)
    # Using a lambda function with filter()
    valid_readings = list(filter(lambda r: r is not None and r >= 0, raw_data))
    
    # 2. Square the valid readings
    # Using a lambda function with map()
    squared_readings = list(map(lambda r: r**2, valid_readings))
    
    # 3. Calculate the sum of the squared readings
    # Using the built-in sum() function
    total_sum = sum(squared_readings)
    
    return total_sum, len(valid_readings), len(squared_readings)

# Step 5: Main Execution Block

# This is where we'll orchestrate the process: generate data, process it, and display the results. We'll use the if __name__ == "__main__": block, which is good practice for scripts that might also be imported as modules.

if __name__ == "__main__":
    print("--- Sensor Data Processing Script ---")
    
    # Generate raw data
    raw_sensor_data = generate_raw_readings(num_readings=30, max_value=150)
    print(f"Generated {len(raw_sensor_data)} raw readings.")
    # print(f"Raw data sample: {raw_sensor_data[:5]}...") # Optional: print a sample
    
    # Process the data
    final_sum, num_valid, num_squared = process_sensor_data(raw_sensor_data)
    
    print(f"Processing complete.")
    print(f"Number of valid readings found: {num_valid}")
    print(f"Number of readings squared: {num_squared}")
    print(f"Sum of squared valid readings: {final_sum:.2f}")
    
    # Example of using a global variable concept (though not strictly needed here)
    # Let's imagine a global configuration for the processing threshold
    PROCESSING_THRESHOLD = 50000
    if final_sum > PROCESSING_THRESHOLD:
        print(f"ALERT: Total sum ({final_sum:.2f}) exceeds threshold ({PROCESSING_THRESHOLD})!")
    else:
        print(f"Total sum ({final_sum:.2f}) is within the acceptable range.")



# Code Explanation and Concepts Used:

# generate_raw_readings function: Demonstrates function definition, parameters, and returning a list. It uses random.random() and random.uniform() from the random module.
# process_sensor_data function: This is the core processing logic.
# Scope: Variables like valid_readings, squared_readings, and total_sum are local to this function.
# Lambda Functions: Used concisely with filter to select valid readings (not None and non-negative) and with map to square each valid reading.
# Built-in Functions: Leverages list(), filter(), map(), and sum().
# if __name__ == "__main__": block: Ensures the main execution logic only runs when the script is executed directly.
# Global Variable Concept: PROCESSING_THRESHOLD is treated as a global constant (though defined within the main block for simplicity here, it could be at the module level).
# Formatted Output: Uses f-strings for clear and readable output, including formatting floating-point numbers to two decimal places (:.2f).


# run COMMAND= python "backend/Building a Simple Data Processing Script/sensor_processor.py"
