
# printing some lines using f strings

name = 'pranamya'
age = int(18)
print(f"\nMy name is {name} and my age is {age}")

# if we didn't used f strings then our code would looked like this :

print ("My name is " + str(name) +" and my age is " + str(age) ) 
name_age_storer = ("my name is {} and my age is {}")
print(name_age_storer.format(name,age)) 


# multiplication table using f strings
# multiplication table of 2 

storer = int(input("Enter the value of number : "))
limit = int(input("Enter till when you want to print the table : "))
for num in range (1,limit+1):
    print(f"{storer} * {num} = {storer*num}")

