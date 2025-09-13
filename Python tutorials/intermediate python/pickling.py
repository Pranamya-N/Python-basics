# PICKLING AND UNPICKLING 

# Pickling is the process of storing the data by converting into the binary system and unpicking is the reverse of pickling 
# it is similar to serialization and deserialization 

import pickle 

class Person:
    def __init__(self,name,age) :
        self.name = name 
        self.age = age 
        
    def display_info(self):
        print(f"Hello my name is {self.name} and my age is {self.age}")
        
person = Person("Pranamya Niroula",19)
        
with open ("person.pkl","wb") as f :
    pickle.dump(person,f)
    
with open ("person.pkl","rb") as f :
    p = pickle.load(f)

p.display_info()
   