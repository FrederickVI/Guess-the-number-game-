#This is a guess the number game.
import random 
import sys
secretNumber = (random.randint(1,20))
print("I am thinking of a number between 1 and 20")

while True:                                      #Option to play the game
    print("Do you want to play the game? yes/no")
    response = input()
    if response == "yes":
        print("")
        break
    elif response == "no":
        print("No one wants to play with me(")
        sys.exit()
    else:
        print("Answer Must Be 'Yes' or 'No'")

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else: 
        break #This condition is the correct guess!

if guess == secretNumber:
    print("Good job! You guessed the number in " + str(guessesTaken) + " guesses")
else:
    print("You failed. The number was" + str(secretNumber))
