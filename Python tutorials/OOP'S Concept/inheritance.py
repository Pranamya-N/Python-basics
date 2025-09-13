# Inheritance in Python is a mechanism where a new class (called a subclass or child class) is created based on an 
# existing class (called a superclass or parent class). The subclass inherits attributes and methods from the 
# parent class, allowing code reuse and extension of existing functionality.
class User: #THIS IS PARENT CLASS
    def login (self):
        print("You logged in")
    
    def register (self):
        print("You Registered")
        
    def logout (self):
        print("You logged out ")
        
class student (User): # THIS IS CHILD CLASS
    
    def enroll (self):
        print("You Enrolled")
        
    def review (self):
        print("Write your review")


#CHILDREN CLASS CAN ACCRSS PARENT CLASS BUT PARENT CLASS CANNOT ACCESS THE CHILDREN CLASS 
student1 = student().login()

# So in this way student class can access the objects of the user class 
# children class cannot access the private members of the parent class directly but can be accessed through 
#getters and setters



