import random

weapon_choices = ["rock", "paper", "scissors"]

while True:
    player_weapon = input("Choose rock, paper or scissors:")

    computer_weapon = random.choice(weapon_choices)

    print("Computer chooses: " + computer_weapon)

    if player_weapon == computer_weapon:
            print("Tie")

    if player_weapon == "rock" and computer_weapon == "scissors":
            print("Winner")

    if player_weapon == "rock" and computer_weapon == "paper":
            print("Loser")

    if player_weapon == "paper" and computer_weapon == "rock":
            print("Winner")

    if player_weapon == "paper" and computer_weapon == "scissors": 
            print("Loser")

    if player_weapon == "scissors" and computer_weapon == "rock":
            print("Loser")

    if player_weapon == "scissors" and computer_weapon == "paper":
            print("Winner")

    keep_playing = input("Keep playing?: y/n ")
    if keep_playing =="n":
        break

