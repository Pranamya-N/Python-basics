# we can read the python file in different way by using the context manager its syntax is as :
# with open ("sample.txt","a") as context_manager :
#     context_manager.write("\nTHIS FILE IS BEING WRITTEN WSING THE CONTEXT MANAGER ")
    
# THE BENEFIT WE GET USING CONTEXT MANAGER IS THAT WE IT AUTOMATICALLY CLOSES THE FILE 
# IN THE READ MODE IF WE WRITE SOME NUMBERS IN THE BRACKET THEN IT WILL READ THE NUMBERS IN THE INDEX OF THE FILE

#READING THE FILE IN THE CHUNKS 
# big_data = ['HELLO PRANAMYA HOW ARE YOU 'for i in range (100)]
# with open ('bigfile','w') as example :
#     example.writelines(big_data)
    
# with open (r'bigfile','r') as reader:
#     chunk_opener = 10
#     while len(reader.read(chunk_opener)) > 0 :
#         print(reader.read(chunk_opener),end = '****')
        

# in this way we can read the chunk of the file at once 

# seek and tell functions 
# .tell function gives you the loacation of what the file is going to point next
# .seek allows you to point to any location in the file 

# USING SEEK FUNCTION TO WROTE THE FILE 
with open ("sample.txt","w") as a:
    a.write("Hello")
    a.seek(0)
    a.write('X') #IT WILL REPLACE H WITH X AND GIVES THE OUTPUT XELLO 
    
