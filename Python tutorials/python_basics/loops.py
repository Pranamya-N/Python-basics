#loops in python
#while loops
# value = int(input("enter the vlaue you want to input :  "))
# while value < 10 :
#     print(value)
#     value += 1
    

# #use of continue and break statements

# user_input = int(input("enter the value you want to input : "))
# while user_input <=10 :
#     print (user_input)

#     user_input += 1
#     if user_input == 5 :
#       break
    
# #use of continue statement 

# user_choice = int(input("enter the value you want to input : "))

# while user_choice <=10 :
    
#     user_choice += 1
#     if user_choice == 5 :
#       continue
#     print(user_choice)

# else:
#     print("the value is :",user_choice)

#   #here the continue statement skips 5 and executes the next code 

# for loops 

#Names = ["pranamya","ronaldo","messi"]
# for x in Names :
#     print(x)


# for x in "biratnagar":
#     print(x)


# for name in Names :
#     if name=="ronaldo":
#       continue
#     print(name)

# print("")



# for name in Names:
#    if name == "ronaldo":
#       break
#    print(name)

  
#structure of ofr loops 
#for (starting number,ending number ,steps)

# for numbers in range (0,9,3):
#     print(numbers)

#multiplication table of numbers 
print("Multiplication table ")
print("")
user_input= int(input("enter the number which which is to be multiplied :   "))
multiplier=int(input("enter the number till which you want your multiplication table :  "))

for i in range (1,multiplier+1):
    product = user_input*i
    print (user_input, "*", i, "=", product)

print("")

for i in range (0,101,5):
 print (i)
 # here the programme prints the nubers between 1 and 100 in the difference of 5 
 # so the for loops are divided into 3 parts and they are for(start,stop,steps)
 #here steps is known as the printing steps as exampled in the above code 
 

# nested for loops 
Name = ["pranamya","manish"]
Action = ["codes","sleeps"]

for name in Name:
   for action in Action :
      print (name + " " + ""+ action)