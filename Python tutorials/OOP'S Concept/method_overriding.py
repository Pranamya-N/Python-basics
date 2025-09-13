# When the same method is used in different class then the methods are called method overriding

class Parent:
    def greet(self):
        return "Hello from the Parent!"

class Child(Parent):
    def greet(self):  # Overriding the `greet` method from the `Parent` class
        return "Hello from the Child!"

# Creating instances of Parent and Child
parent = Parent()
child = Child()

# Calling the `greet` method on both instances
print(parent.greet())  # Output: Hello from the Parent!
print(child.greet())   # Output: Hello from the Child!
