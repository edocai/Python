import random

computer = random.randrange(100)
while True:
    try:
        player = int(input("Choose a number between 1 - 100: "))
        if computer == player:
            print("Correct!")
            break
        elif player < computer:
            print("Guess too low, guess again!")
        elif player > computer:
            print("Guess too high, guess again!")
    except ValueError:
        print("Please enter an integer")
