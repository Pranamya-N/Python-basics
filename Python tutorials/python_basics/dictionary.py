
# dictionary = {"name":"pranamya",
#               "age" :  18,
#                18 : "pranamya" }

# #dictionary1 = {}
# print (dictionary)

# # accesing items in dictionaries

# print (dictionary["age"])

# # lisitng out all the keys

# print(dictionary.keys())

# # listing out all the values stored in a dictionary 
# print(dictionary.values())

# # printing all the items in the dictionaries

# print(dictionary.items())

# # verifiying if the key exists in the dictionary or not 

# print ("name" in dictionary)

# print(dictionary["name"])
# print(dictionary[18])

# # changing the values in dictionaries

# dictionary["18"]="29 november 2005"
# print (dictionary)

# # adding keys in dictionaries 

# dictionary.update({"address":"biratnagar"})
# print(dictionary)

# # removing items from dictionary 

# dictionary.pop ("address")
# print(dictionary)

# # del dictionary [18]
# # print(dictionary)

# # dictionary.clear()
# # print(dictionary)

# # dictionary .clear clears all the items inside the dictionaries but del dictionary deletes the dictionary itself

# #copying items in the dictionaries 
# print("")
# print("")
# dictionary1 = dictionary.copy()
# print(dictionary1)

# # using constructor function 
# print("")
# print("")

# dictionary1 = dict(dictionary)
# print(dictionary1)
# dictionary1[18]={"pranamya niroula"} # adding elements in dictionary
# print(dictionary1)

# #nested dictionaries

# name = {
#     "Name1":input("enter the name of student 1:\t"),
#     "Name2": input("enter the name of student 2:\t")
# }

# age = {
#     "age1":input("enter the age of student 1 :\t"),
#     "age2": input("enter the age of student 2 :\t")
# }

# nested_dictionary = {
#     "name": name ,
#     "age" : age
# }
# print("")
# print("")
# print(nested_dictionary) # this will print all the elements of name and age 

# # accesing the elements and age of the dictionaries 
# print("")
# print("")
# print(nested_dictionary["name"]["Name1"])

# dictionary comprehension using zip (how to convert two lists in one dictionary )
list1 = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
list2 = [22,23,24,25,26,27,28]

result = {i : j for (i,j) in zip(list1,list2) }
print(result)


# more examples 

stock = {"Phone":2,"Laptop":0,"Charger":1}
a = {key : value for (key ,value) in stock.items() if value>0}
print(a)


