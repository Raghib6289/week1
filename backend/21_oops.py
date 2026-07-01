# What is a Class?
# A class is a user-defined data type that serves as a blueprint for creating objects. It encapsulates data (attributes) and functions (methods) that operate on that data. In essence, a class defines the structure and behavior that all objects of that type will share. It's a logical grouping of related properties and actions.

# For example, consider a real-world entity like a 'Car'. A Car has certain characteristics (color, make, model, year) and can perform certain actions (start engine, accelerate, brake, turn). A 'Car' class would define these characteristics as attributes and these actions as methods. The class itself does not represent a specific car; it's the definition of what a car is.

# What is an Object?
# An object, also known as an instance, is a concrete realization of a class. When you create an object from a class, you are essentially creating a specific entity based on the blueprint defined by the class. Each object has its own unique state (values for its attributes) but shares the same behavior (methods) defined by its class.

# Continuing the 'Car' analogy, if 'Car' is the class, then 'my_red_toyota_camry_2023' and 'your_blue_honda_civic_2022' are objects (instances) of the 'Car' class. Each of these objects is a distinct car with its own specific color, make, model, and year, but both can perform the same actions like 'accelerate' or 'brake'.

# Why are Classes and Objects Important?
# The class-object paradigm is crucial for several reasons:

# Modularity: OOP allows you to break down complex systems into smaller, manageable, and self-contained units (objects). This makes code easier to understand, develop, and debug.
# Reusability: Classes can be reused across different parts of an application or even in different projects. This saves development time and reduces redundancy.
# Maintainability: When code is organized into classes and objects, it becomes easier to modify or extend functionality without affecting other parts of the system. Changes within a class are typically isolated.
# Abstraction: OOP allows us to hide complex implementation details and expose only the necessary functionalities. Users of an object only need to know what it can do, not how it does it.
# Real-World Modeling: OOP provides a natural way to model real-world entities and their relationships, making software design more intuitive and aligned with the problem domain.

# What are Attributes?
# Attributes are variables that belong to an object. They store the data associated with a particular instance of a class. Think of them as the properties or characteristics of an object. For our Dog class, attributes could include name, breed, and age.

# What are Methods?
# Methods are functions that are defined within a class and operate on the object's attributes. They define the behavior of an object – what it can do. For our Dog class, methods could include actions like bark(), wag_tail(), or fetch().

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        print(f"A new dog named {self.name} has been created!")

    def bark(self):
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}."

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")    

# Create a Dog object
my_dog = Dog("Buddy", "Golden Retriever", 3)

# Create another Dog object
your_dog = Dog("Lucy", "Beagle", 5)

# Accessing attributes
print(f"My dog's name is: {my_dog.name}")
print(f"Your dog's breed is: {your_dog.breed}")

# Calling methods
print(my_dog.bark())
print(your_dog.describe())

# Using a method that modifies state
my_dog.celebrate_birthday()
print(my_dog.describe())