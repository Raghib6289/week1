colors_set = {"red", "green", "blue"}

# Adding a single element using .add()
colors_set.add("yellow")
print(colors_set) # Output: {'red', 'green', 'blue', 'yellow'} (order may vary)

# Adding multiple elements using .update()
colors_set.update(["purple", "orange"])
print(colors_set) # Output: {'red', 'green', 'blue', 'yellow', 'purple', 'orange'} (order may vary)

# Removing an element using .remove()
# If the element is not found, .remove() raises a KeyError
colors_set.remove("green")
print(colors_set) # Output: {'red', 'blue', 'yellow', 'purple', 'orange'} (order may vary)

# Removing an element using .discard()
# .discard() does not raise an error if the element is not found
colors_set.discard("cyan") # 'cyan' is not in the set, no error occurs
print(colors_set) # Output: {'red', 'blue', 'yellow', 'purple', 'orange'} (order may vary)

# Removing and returning an arbitrary element using .pop()
# Note: Since sets are unordered, the element removed is not predictable.
removed_color = colors_set.pop()
print(f"Removed color: {removed_color}")
print(colors_set)

# Clearing a set
# colors_set.clear()
# print(colors_set) # Output: null

#membership testing
colors_set = {"red", "green", "blue"}

print("red" in colors_set)    # Output: True
print("yellow" in colors_set) # Output: False