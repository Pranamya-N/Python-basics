# SERIALIZATION AND DESERIALIZATION OF CUSTOM OBJECTS 
import json 

class Employee:
    def __init__(self,FirstName,LastName,Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.age = Age
        
    def display_details(self):
        return {
            "Name" : f"{self.FirstName} {self.LastName}",
            "Age" : self.age
        }
        
employee = Employee("Pranamya","Niroula",19)

    
with open ("new.json","w") as f:
    json.dump(employee.display_details(),f,indent = 4)
