# every iterators are iterables but every iterables are not iterators 
# to know if the given object is iterable we should add the items in the dir fuction and if there is __iter__ then 
# the given object is iterators but to know if the object is iterators we should also add the object in dir 
# function and  if there comes __iter__ and __next__ then the function is iterators
# if we put iter function in our iterable then the iterable turns into iterator




"""how doees the for loops work ??  let us understand through an example of list"""

L = [1,2,3,4,5,6]
"""So basically what python does is that it calls iter fuction """
Variable = iter(L)
"""since now the list becomes iterator using iter function so it calls next"""
next(Variable)
next(Variable)

"""here this means that the items in the list are called using next variable and the proces continues 
untill it throws error  """

# Let us make our own for loop 

def my_for_loop (iterable):
    my_iterator = iter(iterable)
    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            break
        
my_list = [1,2,3,4,5,6] 
my_for_loop(my_list)





# WHEN WE PUT ITER ON ITERATOR WE GET A NEW ITER OBJECT WHICH IS THE ITERATOR ITSELF LET US CLEAR THE CONCEPT THROUGH AN EXAMPLE

l = [1,2,3,4,5]
iter_obj = iter(l)
print(id(iter_obj)) 

iter_obj2 = iter(iter_obj)
print(id(iter_obj2)) 
# we get the same output which means that iter obj 2 and iter obj 1 are same 


