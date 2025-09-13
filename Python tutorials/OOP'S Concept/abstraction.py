from abc import ABC, abstractmethod
class Bank (ABC):
    def database (self):
        print("Database connected successfully !!!")
        
    @abstractmethod
    def security (self):
        pass
    
class MobileBankApp(Bank):
    def login(self):
        print("LOGGED INTO THE APP SUCCESSFULLY !!!")
        
#abc = MobileBankApp() If i do this without defining the security in the mobilebank class then the code will not be executed because the decoraor abstractmethod is defined in the 
#parent class of the mobilebank method so to run the code we must write the security code 

    def security(self):
        pass
    
#after defining secururity we can run the programme 

abc = MobileBankApp()

