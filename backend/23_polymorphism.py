# What is Polymorphism?
# In OOP, polymorphism means that a single interface (like a method name) can be used to represent different underlying forms (implementations in different classes). The most common way to achieve polymorphism is through method overriding, which we touched upon in the inheritance section.

# When a subclass provides a specific implementation for a method that is already defined in its superclass, it's called method overriding. Polymorphism allows you to call that method on an object, and the correct version of the method (the one from the subclass) will be executed based on the object's actual type.
    
# How Polymorphism Works with Inheritance
# Polymorphism is most commonly demonstrated through inheritance and method overriding. Let's use our Animal, Dog, and Cat example.

# Demonstrating Polymorphism with the `Animal` Hierarchy
# We have the Animal base class with a speak() method, and the Dog and Cat subclasses that override this method.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of different animal types
buddy = Dog("Buddy")
whiskers = Cat("Whiskers")
generic_animal = Animal("Creature")

# Storing them in a list
animals = [buddy, whiskers, generic_animal]

# Iterating through the list and calling the 'speak' method
# Notice how the correct 'speak' method is called for each object
for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")