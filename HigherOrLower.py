import random
import sys

lives = 10
random_number = random.randint(1, 100)


while lives == 69:
    print("Thi is really funny but I have to kick you from the game sorry...")
    sys.exit()
while lives > 10:
    print(f"Why do you have {lives} lives?")
    sys.exit()

print("Welcome to the 'Higher or Lower' game!")
while lives > 0:
    number = int(input(f"You have {lives} lives left., guess a number between 1 and 100: "))
    if number == random_number:
        print(f"You guess the correct number!")
        sys.exit()
    elif number < random_number:
        print(f"{number} is smaller than the chosen number.")
    elif number > random_number:
        print(f"{number} is larger than the chosen number.")
    
    lives = lives - 1
    
    if lives <= 0:
        print(f"You failed! The correct number was {random_number}")
        sys.exit()
        
