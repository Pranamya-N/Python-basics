import requests
class Indianrailway:
    def __init__(self):
        Name = input ("Enter your name :")
             
        user_input = input(f"""Hello {Name}, How would you like to proceed ?
            1.Enter 1 to know our train live location 
            2.Enter 2 to know the train schedule\n
            """)
        
        if user_input == 1 :
            print("Train live location ")
        else :
            self.train_schedule()
        
        def train_schedule(self):
            train_number = input ("Enter the train number : ")
            self.fetch_data()
            
        def fetch_data(self,train_number):
            