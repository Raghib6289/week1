# How to Implement Inheritance in Python
# In Python, you implement inheritance by specifying the superclass in parentheses after the subclass name when defining the class.

# Hands-On Component 3: Implementing a Basic Inheritance Structure
# Let's create a base class Animal and then derive specific animal classes like Dog and Cat from it.

# Step 1: Define the Base Class (Superclass)

# This class will contain attributes and methods common to all animals.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"An animal named {self.name} ({self.species}) has been created.")

    def speak(self):
        # This is a generic speak method, subclasses will override it
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} is moving."

# Here, Animal has a name and species. It has a generic speak method and a move method.

# Step 2: Define Subclasses that Inherit from `Animal`

# Now, let's create Dog and Cat classes that inherit from Animal.

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the superclass's __init__ method to initialize common attributes
        super().__init__(name, species="Dog")
        self.breed = breed # Add a Dog-specific attribute
        print(f"It's a {self.breed}.")

    # Override the speak method for Dog
    def speak(self):
        return f"{self.name} says Woof!"

    # Add a Dog-specific method
    def fetch(self):
        return f"{self.name} is fetching the ball!"

# Cat class inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the superclass's __init__ method
        super().__init__(name, species="Cat")
        self.color = color # Add a Cat-specific attribute
        print(f"It's a {self.color} cat.")

    # Override the speak method for Cat
    def speak(self):
        return f"{self.name} says Meow!"

    # Add a Cat-specific method
    def purr(self):
        return f"{self.name} is purring contentedly."


# Step 3: Create Instances and Test Inheritance

# Create instances of the subclasses
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "tabby")

# Accessing inherited attributes and methods
print(f"My dog's name: {my_dog.name}")
print(my_dog.move()) # Inherited from Animal

print(f"My cat's species: {my_cat.species}")
print(my_cat.move()) # Inherited from Animal

# Calling overridden methods
print(my_dog.speak())
print(my_cat.speak())

# Calling subclass-specific methods
print(my_dog.fetch())
print(my_cat.purr())

# Trying to call a method from one subclass on another (will cause an error)
# print(my_dog.purr()) # This would raise an AttributeError
