dictionary = {
    101 : {"name":"pranamya","gmail":"pranamya@gmail.com"},
    102 : {"name":"aaditya","gmail":"aaditya@gmail.com"},
    105 : {"name":"jhoncena","gmail":"jc@gmail.com"}
}

for key,value in dictionary.items() :
    print(f"Student ID is : {key}")
    for i in value :
        print(f"{i} is : {value[i]}")
    print("_"* 20)
    
    

