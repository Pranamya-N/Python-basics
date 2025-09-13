import random 
import sys

def global_guess():
    game_count = 0
    playername = None
    
    
    def continue_play():
        #nonlocal game_count
        
        print("\nPlay again ?\n\nPress........\nY to play \nN to exit\n")
        play = input("")
    
        if play.upper() == "Y":
            play_guess_the_number(printrules=False, getmeusername = False)
        
        elif play.upper() == "N":
            sys.exit("\nThank You for playing GUESS NUMBER WITH PYTHON👋👋\n")

        else :
            print("\nInvalid input Error!!! Please choose between 'Y' or 'N'")
            continue_play()

        
    def user_name():
        nonlocal playername
        while True:
            name = input("\nEnter your username : ")
            recheck = input("Please confirm your username : ")
            confirmation = name
            if name == recheck :
                playername = name
                return name
                
            else :
                print("\nERROR !!! the username doesnt match with your innitial username")
                print("Please rey enter your username ")
                continue
    
    def help_user():
        helps = """
        1.If you want to quit the game press Q 
        2.If you want to know the magical number press M 
        3.**PRESS X FOR EXITING HELP SECTION**
        4.**PRESS Q FOR EXITING GAME
        """
        print(helps)    
            
    def rules():
                
        rules = """\n
        THE RULES OF THE GAME ARE LISTED BELOW :
        1. You will choose the range within which I will randomly select a number.
        2. Enter the minimum and maximum numbers for the range when prompted.
         -The range of the number should be in the minimum difference of 5
        3. Guess the number correctly within the specified range.
        4. After each guess, I will provide feedback:
         -'Too high' if your guess is higher than the secret number.
         -'Too low' if your guess is lower than the secret number.
        5. Keep guessing until you find the correct number.
        6.If any help is required press H . This will open help section for you
        7.If you need help with any rules press R . This will open rule section for you 
        8.If you want to quit the game press Q 
        9.**PRESS X FOR EXITING RULES SECTION**
        10.**PRESS Q FOR EXITING GAME
        11.Have fun and enjoy the game!\n
         """
        print("___________________________________________________________________")
        print(rules)
        
    
    
    def play_guess_the_number(printrules = True, getmeusername= True):
        nonlocal game_count,playername
        game_attempt = 0
        if getmeusername:
            user_name()
        
        if game_count == 0 and printrules:
            print("___________________________________________________________________\n")
            print(f" HELLO {playername}👋👋, WELCOME TO GUESS NUMBER WITH PYTHON \n")
            
            rules()
            
         
        while True:
            try :    
                
                lower_limit = int(input("Enter the minimum number for the range : \n"))
                upper_limit = int(input("Enter the maximum number for the range : \n"))
            
                if upper_limit - lower_limit < 5 :
                    print("Error: The range must be at least 5. Please enter a valid range.\n")
                    continue

                elif lower_limit >= upper_limit :
                    print("THE LOWER LIMIT MUST BE SMALLER THEN UPPER LIMIT\n ")
                    continue
                
                break
                
            except ValueError as ve:   
                print(f"Error: PLEASE SELECT VALID INTEGER ")
            
            except Exception as e :
                print(f"AN UNEXPECTED ERROR OCCOURED ")
            
        python_input = random.randint(lower_limit,upper_limit)
        while True:
                 
            user_input = input(f"\nHey {playername} ,Can you guess the magical number : \n")
            if user_input.upper() == 'R':
                rules()
                exit_help = input("")
                while True :
                    
                    if exit_help.upper() == "X":
                        break
                    elif exit_help.upper() == "Q":
                        sys.exit("\nThank You for playing GUESS NUMBER WITH PYTHON👋👋\n")
                    else:
                        print("X FOR EXITING RULE SECTION \n Q FOR EXITING GAME")
                        response_help = input("")
                        continue
                continue    
                    
            elif user_input.upper() == 'H' :
                help_user()
                exit_rule = input("")
                while True :
                    if exit_rule.upper() == "X":
                        break
                    elif exit_rule.upper() == "Q":
                        sys.exit("\nThank You for playing GUESS NUMBER WITH PYTHON👋👋\n")
                        
                    elif exit_rule.upper() == "M":
                        print(f"THE MAGICAL NUMBER IS :{python_input}")
                        game_count += 1
                        print(f"GAME COUNT :{game_count}")
                        continue_play()
                        
                    else:
                        print("X FOR EXITING HELP SECTION \n Q FOR EXITING GAME")
                        response_rule = input("")
                        continue
                continue
            
            elif user_input.upper() == 'M':
                print(f"THE MAGICAL NUMBER IS :{python_input}")
                game_count += 1
                print(f"GAME COUNT :{game_count}")
                continue_play()
                            
            else: 
                try :
                    convert_int = int(user_input)
            
                except ValueError as te :
                    print(f"ERROR : PLEASE SELECT VALID INTEGER")
                    continue
            
                except Exception as e :
                    print(f"AN UNEXPECTED ERROR OCCOURED {e}")
                    continue
    
        
                if python_input == convert_int :
                    print ("\nCONGRATULATIONS !!! YOU WON 🎉🎉\n")
                    game_count += 1
                    game_attempt += 1
                    print(f"GAME COUNT :{game_count}")
                    print(f"ATTEMPTS TAKEN :{game_attempt}")
                    continue_play()
                    
                
                elif convert_int > python_input:
                    print ("\nGUESS THE NUMBER LITTLE LOWER !!! \n")
                    game_attempt += 1
                    continue
                
                elif python_input > convert_int :
                    print ("\nGUESS THE NUMBER LITTLE HIGHER !!!\n")
                    game_attempt += 1
                    continue
                    
                    
        
    return play_guess_the_number

game_logic = global_guess()
game_logic()

if __name__ == "__main__":
    game_logic()





            
            
        
                
            
            
                
        
            
            
        
        
        
        
        
    





    
