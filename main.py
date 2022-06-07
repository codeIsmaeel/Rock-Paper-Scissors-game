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


# import random

# newgame = True

# while newgame == True:

#     def play():
#         choice = ['r', 'p', 's']

#         user = input(
#             "pick a player option; 'r' for Rock, 'p' for Paper, 's' for Scissors:\n")

#         # if user in choice:
#         #     print("Welcome")

#         # else:
#         #     print("Error! Pick player option again")

#         user = user.lower()

#         computer = random.choice(['r', 'p', 's'])

#         if user == computer:
#             return "You and the computer have chosen {}. it is a tie.".format(computer)

#         if is_win(user, computer):
#             return "You have chosen {} and the computer chose {}. You Win!".format(user, computer)

#     #     if is_lost(user, computer):
#     #         return "You have chosen {} and the computer chose {}. You lost!".format(user, computer)

#     # def is_lost(player, opponent):
#     #     # winning conditions: r > s, s > p, p > r
#     #     if (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's') or (player == 'r' and opponent == 'p'):
#     #         return True

#     # use: user and computer not player and opponent

#     def is_win(player, opponent):
#         # return true if the player beats the opponent
#         # winning conditions: r > s, s > p, p > r
#         if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#             return True
#         return False

#     if __name__ == '__main__':
#         play()
