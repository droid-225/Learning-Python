import random

lowest = 1
highest = 100

number = random.randint(lowest, highest)

guess = input(f"Enter a number between {lowest} and {highest}: ")
guesses = 1

while guess != number:
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if lowest > guess > highest:
            print("Guess was out of range!")
            guess = input("\nEnter a number between {lowest} and {highest}: ")
        if guess > number:
            print("Too High!")
            guess = input("\nEnter another guess: ")
        elif guess < number:
            print("Too Low!")
            guess = input("\nEnter another guess: ")
        else:
            break

    else:
        print(f"You must enter a whole number between {lowest} and {highest}")
        guess = input("\nEnter another guess: ")

print(f"\nCorrect! You guessed {number} in {guesses} guesses")
