# Number Guessing Game
# User tries to guess a randomly generated number

import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n=== NUMBER GUESSING GAME ===")
    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid integer")

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break