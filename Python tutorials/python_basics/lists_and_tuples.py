# creating a list 

code = ["Pranamya",18,"kathmandu"]
print(code)

# for finding out the index of the arrays or numers in the list . its indexing starts from 0 
print(code.index("Pranamya"))

# for printing out the length of the list

print(len(code))

# adding elements in the list 
code.extend(["pranamya"])
print(code)

code+=["pranamya"]
print(code)

code.insert(0, "pranamya")

code.remove(18)
print (code)

code [1:1]=["pranamyaaa"]
print (code)

del code[0]
print(code)

code.sort() # it prints the code list in alphabet order
print(code)

nums = [1,2,3,4,5]
print(nums)
nums.reverse()
print(nums)


# tuples

tuple1=("pranamya","biratnagar","18")
tuple2=(1,2,3,4,5)
print(type(tuple1))
newlist=list(tuple1)
# we can add elements in tuple by converting the tuples into the list

newlist.insert (0, "bhaktapur")
newtuple=tuple(newlist)
print(newtuple)