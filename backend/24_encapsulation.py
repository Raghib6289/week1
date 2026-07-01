# What is Encapsulation?
# Think of a capsule containing medicine. The capsule holds the active ingredients and the inactive fillers together, and it protects the medicine from the outside environment. Similarly, in OOP, a class encapsulates its attributes and methods. The key idea is to keep related data and the functions that manipulate that data together within the object.

# Furthermore, encapsulation promotes data hiding. This means that the internal state of an object (its attributes) should not be directly accessible or modifiable from outside the object. Instead, access should be controlled through public methods (getters and setters, or other relevant methods). This protects the object's integrity and prevents unintended modifications.

# How to Implement Encapsulation in Python
# Python does not have strict 'private' keywords like some other languages (e.g., Java, C++). However, it uses naming conventions to indicate intended privacy:

# Public Members: Attributes and methods that are not prefixed with an underscore are considered public and can be accessed from anywhere.
# Protected Members: Attributes and methods prefixed with a single underscore (_) are conventionally considered "protected." This is a hint to other developers that these members are intended for internal use within the class or its subclasses and should not be accessed directly from outside. Python does not enforce this strictly.
# Private Members: Attributes and methods prefixed with double underscores (__) are name-mangled by Python. This makes them harder to access directly from outside the class, effectively providing a form of privacy. The name is transformed into _ClassName__attributeName.

# Example: Implementing Encapsulation with Name Mangling
# Let's create a BankAccount class to demonstrate encapsulation.

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # Public attribute
        self.__balance = initial_balance      # Private attribute (name-mangled)
        print(f"Account {self.account_number} created with initial balance: ${self.__balance:.2f}")

    # Public method to deposit funds
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw funds
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Public method to get the balance (a 'getter')
    def get_balance(self):
        return self.__balance

    # A method to demonstrate accessing a private attribute internally
    def _internal_check_balance(self):
        print(f"Internal check: Current balance is ${self.__balance:.2f}")

# Example usage of the BankAccount class
# Create a bank account
my_account = BankAccount("123456789", 1000.00)

# Accessing public attributes and methods
print(f"Account Number: {my_account.account_number}")
my_account.deposit(500.00)
my_account.withdraw(200.00)
print(f"Current Balance: ${my_account.get_balance():.2f}")

# Attempting to access the private attribute directly (will likely fail or require name mangling)
# print(my_account.__balance) # This will raise an AttributeError

# Using name mangling to access the private attribute (not recommended for regular use)
try:
    print(f"Attempting to access private balance directly: {my_account._BankAccount__balance}")
except AttributeError as e:
    print(f"Error accessing private attribute: {e}")

# Using the protected internal method
my_account._internal_check_balance()