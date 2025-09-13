# EXCEPTION HANDLING 
# THERE ARE FOUR BLOCKS GIVEN TO US BY THE PYTHON FOR EXCEPTION HANDLING WHICH ARE AS FOLLOWS :
#TRY BLOCK : ,EXcept block : , else block: ,finally block :

try:
    first_num = int (input("Enter the furst number: "))
    second_num = int(input("Enter the second number: "))
    div = first_num / second_num
    
except :
    print("something went wromg please enter the valid input ") 
    
else : 
    print("the code is only runnned if there is no exception")
    
finally :
    print(div)
    
# so this is the basic of expection handling you cn also see more of its example in the example of guess 
# the number game loacted in mini project 

#use of raise keywod in python

try :
    age = int(input("Enter your age : "))
    if age <= 0 :
        raise ValueError
        print (f"Your age is :{age}")
        
    
except ValueError:
    print("Please enter your valid age !!!! ")
    
print("Rest of your code ")

# So Raise keyword is used when we have to display our own exception message 

# CREATING USER DEFINED EXCEPTION 
