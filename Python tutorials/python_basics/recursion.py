# when the function is called inside the function then it is called recursion 

# def continue_playing():
#     print("\nDo you want to continue playing ?\nPress Y to play Press N to exit\n")
#     play = input("Enter your response : ")
  
#     if play.upper() == "Y":
#         return play_rock_paper_scissor()
    
#     elif play.upper() == "N":
#         sys.exit("\nThank You for playing Rock Paper Scissor👋👋\n")

#     else :
#         print("Invalid input Error!!! Please choose between 'Y' or 'N'")
#         continue_playing()
    
# refrence is mini projects (Rock Paper Scissor)


#factorial of the number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    else :
        return n*factorial(n-1)
    
num = int(input("Enter the number :    "))
if num < 0 :
    print("Invalid input we can only calculate the factorial of the positive number ")
    
else :
    result = factorial(num)
    print("The factorial of the number is : " + str(result))
    

