# import random

# options = ("rock", "paper","scissors")
# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("Its a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")

#     play_again = input("Play again? (y/n): ").lower()
#     if not play_again == "y":
#         running = False

# print("Thanks for playing!")


#another method
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSOR = 3

# print("")
# player_choice =input(
#     "Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n"
# )

# player = int(player_choice)

# if player < 1 | player > 3:
#     sys.exit("You must enter 1, 2, or 3.")

# computer_choice = random.choice("123")

# computer = int(computer_choice)

# print("")
# print("You chose " + str(RPS(player)).replace('RPS.','')+ ".")
# print("Python chose " + str(RPS(computer)).replace('RPS.','')+ ".")
# print("")

# if player == 1 and computer == 3:
#     print("🎉 You win!")
# elif player == 2 and computer == 1:
#     print("🎉 You win!")
# elif player == 3 and computer == 2:
#     print("🎉 You win!")
# elif player == computer:
#     print("🤔 Tie game!")
# else:
#     print("🐍 Python wins!")


#rps another method

import sys
import random
from enum import Enum

def rps(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        player_choice =input(
            f"\n{name},please enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

        if player_choice not in ["1","2","3"]:
            print(f"{name},please enter 1, 2, or 3.")
            return play_rps()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)
        
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉{name} You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉{name} You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{name} You win!"
            elif player == computer:
                return "🤔 Tie game!"
            else:
                player_wins += 1
                return f"🐍 Python wins!\nSorry, {name}..😢"

        game_result = decide_winner(player,computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count:  {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\nPlay_again, {name}?")

        while True:
            play_again = input("\n Play again? \nY for Yes or \nQ to Quit  \n")
            if play_again.lower() not in ["y","q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🙌")
            print("Thank you for playing!")
            sys.exit(f"Bye{name}! 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar= "name",
        required = True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
