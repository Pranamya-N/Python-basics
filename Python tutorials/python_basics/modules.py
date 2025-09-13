
# from scope import student1
# from closures import storer

# print(student1)
# in this way we can import or create our own modules but the modules 
# need to be in the same directory

import functions
print("starts here\n")
functions.sum_two_nums(3,4)
functions.number(2)
functions.pizza_order("Large","Pineapple","Olive",order = "pizza",Delivered_by = "Pizza house",Delivered_to = "Pranamya Niroula")

#print(functions.pizza_order.__doc__)

print("\nends here")


#Note : when making module always put the functions into if __name__ == "__main__" to avoid
#unnecessary running of the programme 
#__doc__ is very usefull when mporting functions it is used to give description about the function it is written just below the defination 
# of function and is defined under """__doc__ is written here""" it's full name is docstrings 