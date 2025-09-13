# no duplicates are allowed in sets 

#initializing the set 

set = {1,0,2,1,3,4,5,6,7,8,9,10}
print (set)
# it automatically arranges the data in alphabetical order  

# in set true is the dupliacte of 1 and false is the dubicate of 0

set1={2,False,3,True,1,0}
print(set1)

# the function works in such a way that true and false are the duplicates of 1 and 2 and it print the set in sequence 
#which means that if in the set there is 1 at the first index then it will ignore true and vice versa and there 
#goes same for false and 0

print(2 in set)
#in this way we can check if the number is in the set or not

# we cannot check the index of the elements in the sets 

# adding elements from one set to anothes set 

set1.update(set)
print(set)

# we can also add elements in the sets by using add function

set1.add(11)
print(set1)

# we can add dictionaries,lists and tuples as well in the sets 

dictionary=[12,13,14,15,16]
set1.update(dictionary)
print(set1)

# merging two sets to create a new set by using union function

one={1,2,3}
two={4,5,6}

my_new_set= one.union(two)
print(my_new_set)

# printing only the duplicates in the sets

three = {1,2,3,4}
four = {2,3,4,5}
three.intersection_update(four)
print(three)

print("")
print("")

#printing only the elements that are not the duplicate 
five={5,6,7}
six={5,6,7,8}
five.symmetric_difference_update(six)
print(five)

my_name={"Pranamya Niroula"}



