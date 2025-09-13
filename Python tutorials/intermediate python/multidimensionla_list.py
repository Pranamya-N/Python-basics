multidimensional_List = [[1,2,3],"Pranamya",[3,4,5]]
# SO THIS IS THE MULTIDIMENSIONAL LIST AS IT HAS LIST INSIDE THE LIST SO TO ACCESS WE CAN DO THE FOLLOWING 

print(multidimensional_List[0]) #THIS WILL ACCESS THE LIST STORED IN THE ZEROTH INDEX [1,2,3]
print(multidimensional_List[0][1]) # THIS WILL ACCESS THE FIRST ELEMENT OF THE FIRST LIST 

#SO THIS IS HOW WE CAN ACCESS THE ELEMENTS OF THE MULTIDIMENSIONAL LIST 

#APPENDING ANOTHER LIST TO THE MULTIDIMENSIONAL LIST

new_list = [6,7,8]
multidimensional_List.append(new_list)
print (multidimensional_List)

#ZIP FUNCTION IN PYTHON
#The zip() function in Python is used to combine multiple iterables (such as lists, tuples, etc.) element-wise. 
#It pairs elements from each iterable based on their position (index), creating tuples of corresponding elements.

#EXAMPLE OF ZIP FUNCTIONS 
username = ("Pranamya","Aaditya",)
password = ("pranamya@#","aaditya@#")
stored = zip(username,password)

for i,j in stored :
    print(f"Username : {i} \tPassword : {j}")
    
#THIS IS HOW THE ZIP FUNCTION WORKS 
