
# scope of local and global variables
name = "pranamya"
age = 18

def student1():
    college = "KU"
    #age += 1
    #here we cannot directly put age as age is not defined inside the function 
    #so variable ko name je sukai vaye ni farak pardaina tedi function vitra hami le variable declare garem vane
    # teo local variable huncha 
    # tara we can access global variable using global keyword inside the function as mentioned below

    global age 
    age += 1 
    print(age)
    print(college)
    def student2():
        nonlocal college
        college = "TU"
        global age 
        age += 2
        print(college +"\n"+ str(age) )
    student2()

student1()

# if the function is nested function then we can access the variables of the parent function by using notlocal
# keyword and we can also access the global values inide the nested function by using global keyword but the 
# problem is that if we accesed the global variables in the parent function then the global function will work
# from the parent function like here in the example student 1 is the parent function and student 2 is the 
# child function then we accsed global age inside the child function then it printed by acting parent function as a 
# global function  
