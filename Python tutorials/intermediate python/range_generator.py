"""same thing we had done with the iteratirs and now we are going to do the same thing using generators 
so basically generators are desined to do iteration bt in shorter ways """

def my_Range (start,end):
    for i in range (start,end+1):
        yield i
for i in my_Range(15,30):
    print(i)