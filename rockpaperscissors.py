import random

choices = ["rock","paper","scissors"]

while True:

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Choose Rock or Paper or Scissors").lower()


    if player == computer:
        print("Computer : "+computer )
        print("Player : "+player)
        print("Wow You both chose the same!! It's a TIE !!")
    elif player == "rock":
        if computer == "scissors":
            print("Computer : "+computer )
            print("Player : "+player)
            print("Rock crushes Scissors!! You WON !!!")
        elif computer == "paper":
            print("Computer : "+computer )
            print("Player : "+player)
            print("Paper wraps Rocks !! You LOST :(")
    elif player == "paper":
        if computer == "scissors":
            print("Computer : "+computer )
            print("Player : "+player)
            print("Scissors cuts Paper !! You LOST :(")
        elif computer == "rock":
            print("Computer : "+computer )
            print("Player : "+player)
            print("Paper wraps Rocks !! You WON !!!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer : "+computer )
            print("Player : "+player)
            print("Rock crushes Scissors!! You LOST :(")
        elif computer == "paper":
            print("Computer : "+computer )
            print("Player : "+player)
            print("Scissors cuts Paper !! You WON !!")
    x = input("Do you want to Play again Enter Yes or No").lower()
    if x == "no":
        break

