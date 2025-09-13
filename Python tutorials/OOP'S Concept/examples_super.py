class Phone:
    def __init__(self,brand,model_no,camera):
        print("Inside phone constructor")
        self.brand = brand
        self.model_no = model_no
        self.camera = camera
        
class Smartphone(Phone):
    def __init__(self,brand,model_no,camera,os,ram):
        print("inside the first part of the smartphone class")
        super().__init__(brand,model_no,camera)
        self.os = os
        self.ram = ram 
        print ("Ending of the smartphone constructor")
        
phone = Phone("Realme",123456,"12MP")
smartphone = Smartphone("Samsung",54321,"120MP","Android","16GB")

print(smartphone.brand)

