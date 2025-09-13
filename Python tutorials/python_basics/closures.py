# so closure is the method to access the nested function in the global scope by returning the nested 
#function to the parent function and storing the parent function to the variable 
# here parent_function() acceses the primary function whereas parent_function accesses the
#memory address of the parent_function() 

def parent_function():
    print("this is the parent function")
    
    def primary():
        print("this is primary function")
    return primary

storer = parent_function()

print(storer())  # Call the primary function directly using storer
