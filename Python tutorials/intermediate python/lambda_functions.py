# LAMBDA FUNCTIONS 

#BASICALLY LAMBDA ARE THE ANOYNOMOUS FUNCTIONS USED IN PYTHON PROGRAMMING ITS SYNTAX IS 

#   LAMBDA ARGUMENTS : EXPRESSION 

#SOME BASIC  EXAMPLES OF LAMBDA FUNCTIOS 

squared = lambda x : x**2
print(squared (2))

multiply = lambda x,y : x*y
print(multiply(2,3))

even_odd = lambda x: "Even" if x % 2 == 0 else "odd"
print(even_odd(3))

# IT IS ONLY IN ONE LINE AND IT IS NOT USED FOR THE CODE REUSABILITY AND IT HAS NO NAME 
# WHY LAMBDA FUNCTIONS ?? IT IS USED WITH HIGHER ORDER FUNCTIONS 

# WRITE A LAMBDA FUNCTIONS WHICH GIVE YOU THE SUM OF THE NUMBERS DIVISIBLE BY 2 DIVISIBLE BY 3 AND ODD NUMBERS 

list = [23,24,25,26,27,28,29]
x = lambda x : x % 2 == 0 
y = lambda y : y % 3 == 0
z = lambda z : z % 2 == 0

def return_value (func,list):
    sum = 0 
    for i in list :
        if func(i):
            sum += i
    return sum 
    
print(f"\nEVEN SUM : {return_value(x,list)} \nODD SUM : {return_value(y,list)} \nDIVIDED BY 3 SUM : {return_value(z,list)}\n")
