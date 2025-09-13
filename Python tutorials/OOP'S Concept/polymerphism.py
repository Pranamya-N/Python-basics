# Polymorphism: Different objects responding to the same method

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# Polymorphism: Different objects responding to the same method
def animal_sound(animal):
    print(animal.sound())

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Using the same function to handle different types of objects
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow

