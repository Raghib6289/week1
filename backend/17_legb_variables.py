# Python follows the LEGB rule to resolve variable names:

# L (Local): The innermost scope, containing local variables defined within the current function.
# E (Enclosing function locals): If the current function is nested inside another function, this scope includes variables from the outer function(s).
# G (Global): The scope containing variables defined at the module level.
# B (Built-in): The outermost scope, containing pre-defined names like print, len, str, etc.
# When you refer to a variable, Python searches for it in this order: Local → Enclosing → Global → Built-in. The first place it finds the name, it uses that variable.

# Example Illustrating LEGB:

x = "global x"

def outer_function():
    x = "enclosing x"
    
    def inner_function():
        x = "local x"
        print(f"Inside inner_function: {x}") # Local scope

    inner_function()
    print(f"Inside outer_function: {x}") # Enclosing scope

outer_function()
print(f"Outside functions: {x}") # Global scope