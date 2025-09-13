# HIGHER ORDER FUNCTIONS (MAP FILTER AND REDUCE FUNCTIONS)

#Map functions in python 

# SYNTAX IS MAP (FUNCTIONS , ITERABLES )

listt = [1,2,3,4,5,6,7,8,9]
double = list(map ((lambda x : x ** 2),listt))
print(double)

# WE CANNOT CALL MAP FUNCTIONS DIRECTLY WE HAVE TO CONVERT IT IN THE LIST FIRST 

#MAP FUNCTION TO PRINT THE EVEN OR ODD LISST 
listtt = [1, 2, 3, 4, 5, 6]

# Just map to print even numbers, ignore the result
even_odd = list(map(lambda x: (print(x) if x % 2 == 0 else None), listtt))
print(even_odd)



# FILTER FUNCTION IN PYTHON 

# so the main differenc ebetween filter and map is that it iterates all ovet the iterator but the map performs only in the certain condition 
abc = [1,2,3,4,5,6,7,8,9,10]
storer = list(filter(lambda x:x >= 4,abc))
print(storer)


# REDUCE FUNCTION 
# WHAT REDUCE DOES IS THAT IT REDUCES THE LIST IN SMALL PART AND PERFORMS THE OPERATION 
import functools
deff = functools.reduce(lambda x,y : x+y,abc)
print(deff)

# SO IN THIS WAY REDUCE WORKS 
