import random

player_win = 0     #accessed as global variables
pc_win = 0

def validate_name(): #validating the name and error handling. If the name contains numbers, you will get error. 
    name = input(" Please write your name to start the game.")
    if name.isalpha:
        return name
    else:
        print("Error. Please write your name not a number.")

   
def check(player_move, pc_move):#check of results from player and pc inputs
    global player_win, pc_win #using global keyword to acces these variables
    if player_move == pc_move :
        print("It's a tie!")
    elif (player_move =="Rock" and pc_move == "Scissors") or \
        (player_move == "Paper" and pc_move == "Rock") or \
        (player_move == "Scissors" and pc_move == "Paper"): #using or to not making code overly long. This way it's short and easy to figure out
        print("You win")
        player_win += 1
    else:
        print("Pc win")
        pc_win += 1
    return player_win, pc_win #returning the value to update variables
def play_game():
    
    while True:
        pc_choice = ["Rock", "Paper", "Scissors"] #list of option for pc 
        player_move = input("Please write your move (Rock, Paper, Scissors) or End to close the game.").capitalize()
        if player_move == "End": #the option of ending the game first. Otherwise it wouldn't work
            print(f"You won {player_win} times, and Pc won {pc_win} times")
            break
            
        elif player_move not in ["Rock", "Paper", "Scissors"]: #Error handling for player input
            print("Error. Please write only 1 of the 3 options.(Rock, Paper, Scissors)")
            continue
        else:
            pc_move = random.choice(pc_choice) #random picking choice of pc
            print("Pc choose", pc_move)
           
        check(player_move, pc_move) #calling check function

def main():
    print("Hello. Welcome to the game Rock, Paper, Scissors")
    name = validate_name() #calling validate_name function to check the name. The game won't start unless you don't have your name right 
    print(f"Nice to meet you {name}, let's play")
    play_game()#calling the play game function. 

if __name__ == "__main__":#This line is used to check if the code is run directly as the main program.
    main() #without this game won't even start. 

