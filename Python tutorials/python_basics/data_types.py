# to check the data types

name="pranamya"
print(type(name))
print(type(name)==str)

firstname= "leonel"
lastname="messi"

full_name=firstname  +" "+  lastname
print(full_name)

# changing data types into strings

int=str(1950)
print(type(int))
#this is how we can write the multiline strings
multiline = '''my 
            name        
                is  
                    pranamya niroula
'''
print(multiline)


# .upper changes the value into uppercase while .down changes the value into lowercase
# we can also escape the special characters by writing \
#.title makes all the starting words in the string capital(for example if there is the statement hello you then .title makes the statement into Hello You)
#. replace replaces the word (the syntax of .replace is given as ) 
print(multiline.replace ("pranamya","PRANAMYA"))

import math
print (math.pi)

