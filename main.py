import random


def getnumber():
    generated_number = random.randint(1,3)
    return generated_number
    
    

def generate_option(num):
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    else:
        return "Scissors"
    
def my_option():
    print("Enter your Option")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    option_me = int(input())
    option = generate_option(option_me)
    return option

def compare_option(comp, ply):
    if comp == ply:
        return "Draw"
    elif comp == "Rock" and ply == "Paper":
        return "You Win"
    elif comp == "Rock" and ply == "Scissors":
        return "You Lose"
    elif comp == "Paper" and ply == "Rock":
        return "You Lose"
    elif comp == "Paper" and ply == "Scissors":
        return "You Win"
    elif comp == "Scissors" and ply == "Rock":
        return "You Win"
    elif comp == "Scissors" and ply == "Paper":
        return "You Lose"
    else:
        return "Invalid Option"


    



print("Start Game")
turn = True
ply_point = 0
comp_point = 0

while turn == True:
    turn += 1
    get_number = getnumber()
    num_option = generate_option(get_number)
    ply_option = my_option()
    round_result = compare_option(num_option, ply_option)
    if round_result == "You Win":
        ply_point += 1
    elif round_result == "You Lose":
        comp_point += 1
    print("Round Result: " + round_result)
    print("Player Points: " + str(ply_point))
    print("Computer Points: " + str(comp_point))  
    print("Do you want to play again? (Y/N)")
    play_again = input()
    if play_again == "N":
        turn = False
        print("Game Over")
        print("Final Result")
        print("Player Points: " + str(ply_point))
        print("Computer Points: " + str(comp_point))
        if ply_point > comp_point:
            print("You Win")
        elif ply_point < comp_point:
            print("You Lose")
        else:
            print("Draw")
    else:
        turn = True    
    print ("---------------------------------------")
    







