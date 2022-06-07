import random


new_game = True

while new_game == True:

    choices = ["r", "p", "s"]

    computer = random.choice(choices)
    player = input(
        "pick a player option; 'r' for Rock, 'p' for Paper, 's' for Scissors \n")
    player = player.lower()

    if player == choices:
        pass
    # print("The computer chose", computer)

    if computer == player:
        print("You:", player, "Computer:", computer, "It is a tie!")

    elif (player == 'r' and computer == "s") or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print("You:", player, "Computer:", computer, "You Win!")

    elif (player == 's' and computer == "r") or (player == 'p' and computer == 's') or (player == 'r' and computer == 'p'):
        print("You:", player, "Computer:", computer, "Computer Wins!")

    else:
        print("Error! Pick player option again")
