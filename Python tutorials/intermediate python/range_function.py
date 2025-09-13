# LET US MAKE OUR OWN RANGE FUNCTION

class My_Range :
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
       return Range_iterator(self)
   
class Range_iterator:
    def __init__(self,limits):
       self.limits = limits    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.limits.start >= self.limits.end:
            raise StopIteration
        
        current = self.limits.start 
        self.limits.start += 1
        return current
    
for i in My_Range(1,5):
    print(i)

