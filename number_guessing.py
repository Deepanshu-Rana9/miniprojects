# perfect number guessing game
import random
print("--------------------------------")
print("Welcome to the perfect number guessing game!")
print("You have to guess about a number what i am thinking between 1 to 1005.")
number = random.randint(1,100)
guess_num = -1
while guess_num != number:
    guess_num = int(input("Enter your number: "))
    if guess_num==number:
        print(f"Congratulations! You guessed a perfect number: {number}.")
    else:
        if guess_num>number:
            print("Think about a lower number.")
        elif guess_num<number:
            print("Think about a higher number.")
        else:
            print("Something went wrong!")





