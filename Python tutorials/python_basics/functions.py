# declaring functions in python 
# def hello_world() :
#     print("hello world")

# hello_world()

# def sum(num1,num2):
#     if (type(num1) is not float or type(num2) is not float):
#         return 0;
#     return num1+num2

# print("enter the numer you want to input")
# storage = sum(float(input()),float(input()))
# print("sum = "+ str(storage)) 


#args and kwargs 
# *args creates tuples in the function while **kwargs creates dictionary in the function 
#__doc__ is very usefull when mporting functions it is used to give description about the function it is written just below the defination 
# of function and is defined under """__doc__ is written here""" it's full name is docstrings 
# here this function places order..... is docstrings 
def pizza_order(size,*toppings,**delivery_details):
    """
    this function places order for pizza 
    args:
    size (str) = Size of pizza (eg : small,medium,large) 
    *toppings (tuple) = toppings of pizza 
    ** delivery_details (dictionary) = delivery details (eg : order : , delivered to :,delivered by :)
    """
    
    
    print("\nYou ordered a "+ size +" sized pizza having following toppings :\n ")
    for topping in toppings:
        print(topping.capitalize())
        
    print("\nYour pizza delivery details are listed below :\n ")
    
    for key,value in delivery_details.items() :
        print(key.replace('_', " ").capitalize() + ":" + value.capitalize())

pizza_order("Large","Pineapple","Olive",order = "pizza",Delivered_by = "Pizza house",Delivered_to = "Pranamya Niroula")
print ("\n")


# def add_one (num):
#     if(num<=9):
#          return num+1
         
#     total = num+1
#     print(total)
#     return add_one(total)
         
# my_new_total = add_one(0)
# print(my_new_total)

def number (num):
    for number in range (0,9):
        print(f"the numbers in range are {number}")
        


def sum_two_nums(a,b):
    sum = a+b
    print(f"\nThe result of sum of the nubers are : {sum}\n")
    return sum


if __name__ == "__main__" :
    sum_two_nums(1,2)
    number(1)
    pizza_order("Large","Pineapple","Olive",order = "pizza",Delivered_by = "Pizza house",Delivered_to = "Pranamya Niroula")
    


