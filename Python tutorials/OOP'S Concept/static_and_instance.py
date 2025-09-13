#  STATIC(CLASS VARIABLES ) = THE VALUE DOES NOT CHANGES UNLESS MODIFIED 
#  INSTANCE VARIABLES = THE VALUE CHNAGES WITH THE CHANGE OI THE OBJECTS 
    
class Employee :
    Company_name = "Pathao"  #This is class variable 
    def __init__(self,name,address):
        self.name = name
        self.address = address
        #Thsis is instance variable 

#CLASS METHOD IS THE SPECIAL IN BUILT DECORATOR WHICH HELPS US TO ACCESS MODIFY THE CLASS VARIABLES IT TAKES ARGUMENTS AS CLS AND TO ACCESS IT WE TYPE 
#CLS.CLASSVARIABLENAME
    
    @classmethod
    def get_company_name (cls):
        print(f"Company name is :{cls.Company_name}")
        
    def details(self):
        print(f"Employee Name is {self.name} \n Employee address is {self.address} ")
        
#WE CAN ALSO ACCESS THE MEMBERS OF ONE CLASS IN OTHER CLASS BY USING STATIC METHOD
#This will change the address of smair 
class Change :
    @staticmethod
    def change_address (obj):
        obj.address = 'DHARAN'
        obj.details()
        
        
Samir = Employee("Samir","Biratnagar")
Change.change_address(Samir)

    
        
