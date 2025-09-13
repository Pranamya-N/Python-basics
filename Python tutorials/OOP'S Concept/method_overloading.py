# technically method overloading doesnot exists in python but we can achieve the result 
# method overloading is the process by which we can use one function to achieve different result by giving different
# inputs 
class  Area :
    def area (self,l,b=0):
        if b == 0:
            print(f"Area of circle : {3.14 * l *l}")
        
        else :
            print(f"Area of Rectangle : {l*b}")
            
shape = Area()
shape.area(2,3) 