# super is the method in polymerphism in which we can access the construstors and objects of the parnet class by
# using the method super().method()

class Parent:
    def greet(self):
        return "Hello from the Parent!"

class Child(Parent):
    def greet(self):  # Overriding the `greet` method from the `Parent` class
        print(super().greet()) # THIS WILL PRINT HELLO FROM THE PARENT
        return "Hello from the Child!"

# Creating instances of Parent and Child
parent = Parent()
child = Child()

# Calling the `greet` method on both instances
print(parent.greet())  # Output: Hello from the Parent!
print(child.greet())   # Output: Hello from the Child!
