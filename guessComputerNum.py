import random

print("Welcome to the number guessing game!")
maxNum = int(input("What would you like the range to be? (1 - ?): "))

#defining a function for the guess
def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    
    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < randomNumber:
            print("Ohhhhh. Too low. Try again.")
        elif guess > randomNumber:
            print("Ouch. Too high. Try again.")
        
    print(f"You're right! The number was {randomNumber}!")

guess(maxNum)