# Generators are functions that use the yield keyword to return values one at a time, allowing them to produce a sequence 
# of values over time, rather than computing them all at once and sending them back at the end.

# yield keyword keeps the numbers in memory for eg

def dissplay():
    yield "first yield statement"
    yield "Second yield statement"
    
abc = dissplay()
print(next(abc))
# When the first yield statement is executed it keeps in memory to prin the second yield statement so  
# when i do print (next(abc)) it prints the second yield statement

print(next(abc))

"""same thing als0 happenswith looping statement for eg there are 5 yield statement and if i print 2 yield statement manually 
and make the loop for next three statements then the loop execute from the third statement only """