#NORMAL METHOD FOR STORING THE DATA IN THE LISTS 

squares =  []
for i in range (1,6):
    squares.append(i*i)
print(squares)

#LIST COMPREHENSION METHOD 
squares = [i*i for i in range (1,6)]
print(squares)

#Table generation with list comprehension 
a = int(input("Enter the value for which you want to generate the table : "))
table = [a*i for i in range (1,11)]
print(table)

abc = [x for x in range (11) if x%2 == 0 and x != 0]
print(abc)

# LIST COMPREHENSIONS ARE BAD IF WE USED THEM IN THE WORK WHICH IS RELATED TO MEMORY BECAUSE IT OCCUPIES A LOT OF MEMORY AS ALL THE DATA OF THE 
#LISTS ARE LOADED IN THE MEMORY FIRST BUT WHEN WE USE ITERATORS LIKE FOR LOOP IT LOADS ONE OBJECT IN THE MEMORY AT A TIME

    