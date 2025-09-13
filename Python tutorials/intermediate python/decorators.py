# a decorator is the function in the python which takes anothr function as an input add functionality and 
# returns it

# we are making a decorators to print the time taken by the function to be executed 

import time 
def time_measure (func):
    def wrapper (*args):
        start = time.time()
        func(*args)
        print(f"The time taken by {func.__name__} to execute is {time.time() - start} sec")    
    return wrapper 

@time_measure

def hello (name):
    print (f"Hello {name}")
    time.sleep(2)
    
hello("Pranamya")


# writing a decorator to weather to print or not that data type 

def check_datatype(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
            else :
                raise TypeError("Please enter the integer datatpe")
        return inner_wrapper
    return outer_wrapper
@check_datatype(int)            
def square (number):
    print(number * number)
    
square(4)

