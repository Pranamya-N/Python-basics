# THIS METHOD IS TO WRITE IN THE FILE WHICH IS NOT CREATED YET 
# f = open('sample.txt','w')
# f.write("HELLO WORLD !!")

# f.close()
#after doing close function we cannot write anything in the file
# if you want to append the file then you should write a in the place of w which means append 

# Read files 
abc = open (r'C:\Users\Pranmaya Niroula\Desktop\python programming\Python tutorials\intermediate python\sample.txt',"r")
var = abc.read()
print(var)
abc.close()

# IN THIS WAY YOU CAN READ THE FILES BUT WHEN YOU COPY THE PATH YOU SHOULD ADD R IN THE INNITIAL 


