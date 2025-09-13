import sys 
class Atm :
    def __init__(self) :
        self.__pin = ""
        self.__balance = 0
        self.menu()
    
    def menu(self):
        while True:
            user_input = input ("""
                                HELLO HOW WOULD YOU LIKE TO PROCEED 
                                1. ENTER 1 FOR CREATING YOUR ATM PIN 
                                2. ENTER 2 DEPOSITING AMOUNT IN YOUR BANK
                                3. ENTER 3 FOR CHECKING YOUR BANK BALANCE
                                4. ENTER 4 TO WITHDRAW YOUR AMOUNT 
                                5. ENTER 5 TO EXIT THE SYSTEM  \n
                                """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit_amount()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.withdraw_amount()
            elif user_input == "5":
                break
            else :
                print("PLEASE SELECT THE VALID OPTION !!!")
                
    
    def create_pin(self):
        self.__pin = input ("SET YOUR PIN : ")
        print("PIN SET SUCCESSFULLY !!!")
        #self.menu()
        
    def deposit_amount(self):
        pin_storer = input("ENTER YOUR PIN : ")
        if pin_storer == self.__pin:
            amount = int(input("Enter the amount you want to deposit in your account : "))
            self.__balance += amount
            print(f"TRANSACTION SUCCESSFULL !!")
        else:
            print("Invalid pin please enter the valid pin ")
        
    def check_balance(self):
        pin_storer = input("ENTER YOUR PIN : ")
        if pin_storer == self.__pin:
            print(f"Your current balance is :{self.__balance}")
        else:
            print("INVALID ")
            
    def withdraw_amount(self):
        pin_storer = input("ENTER YOUR pin : ")
        if pin_storer == self.__pin:
            amount = int(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW : "))
            if amount > self.__balance:
                print(" INSUFFICIENT AMOUNT ")
            elif amount < self.__balance:
                self.__balance -= amount
                print("TRANSACTION SUCCESSFULL !!")
            print(f"YOUR CURRENT BANK BALANCE IS :{self.__balance}")
        else :
            print("INVALID pin !!!")
           

if __name__ == "__main__":
    
    Pranamya = Atm()



