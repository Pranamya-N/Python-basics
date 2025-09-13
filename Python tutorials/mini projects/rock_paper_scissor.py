#rock_paper_scissor game in python
import random
import sys
   
def global_rock_paper_scissor():
    game_count = 0
    python_win_count = 0
    user_wins_count = 0
    draw_count = 0

    def continue_playing():
        nonlocal user_wins_count,draw_count,python_win_count,game_count

        print("\nPlay again ?\n\nPress........\nY to play \nN to exit\n")
        play = input("")
    
        if play.upper() == "Y":
            return play_rock_paper_scissor()
        
        elif play.upper() == "N":
            sys.exit("\nThank You for playing Rock Paper Scissor👋👋\n")

        else :
            print("\nInvalid input Error!!! Please choose between 'Y' or 'N'")
            continue_playing()

    def play_rock_paper_scissor():
        nonlocal user_wins_count,draw_count,python_win_count,game_count
        print("\n***** \nWelcome to the game of Rock Paper Scissor\n*****\n")
        print("Enter..........\n1 for Rock🪨\n2 for Paper📃\n3 for Scissor✂️\n")
        Choices=["Rock🪨","Paper📃","Scissor✂️"]

        user_input = input("Enter your choice :  ")
        python_input = random.randint(1,3)

        if user_input not in ["1","2","3"]:
            print("Invalid input error!!!\nYou must input the number among (1,2,3) \n")
            
            continue_playing()
            
        
        user_input = int(user_input)
        print("\nYou choosed : "+ Choices[user_input-1])
        print("Python choosed : "+ Choices[python_input-1])

        if user_input == 1  and python_input == 3:
            
            print("\nCongratulations!! you won 🍾")
            
            user_wins_count += 1

        elif user_input == 3  and python_input == 2:

            print("\nCongratulations!! you won 🍾")
            
            user_wins_count += 1

        elif user_input == 2  and python_input == 1:

            print("\nCongratulations!! you won 🍾")
            
            user_wins_count += 1

        elif user_input==python_input :
            
            print("\nOpps!! the game is tie 😔")
            
            draw_count += 1

        else:
            print("\nOpps!! python won 😔")
            
            python_win_count += 1

        game_count += 1
        
        print("\nGame count =" + str(game_count))

        print("\nPyhton wins =" + str(python_win_count))

        print("\nUser wins =" + str(user_wins_count))

        print("\nDraw =" + str(draw_count))

        continue_playing()

    return play_rock_paper_scissor

playgame = global_rock_paper_scissor()


playgame()

if __name__ == "__main__" :
    playgame = global_rock_paper_scissor()
    playgame()



