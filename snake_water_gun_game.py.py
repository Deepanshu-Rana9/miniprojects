import random
'''
snake = 1 
water = -1
gun = 0
'''

computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake",-1: "water",0: "gun"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw.")

else:
    if(computer == -1 and you == 1):
        print("You Win!!")
    elif(computer == -1 and you == 0):
        print("You lose!!")
    elif(computer == 1 and you == 0):
        print("You win!!")
    elif(computer == 1 and you == -1):
        print("You lose!!")
    elif(computer == 0 and you == 1):
        print("You lose!!")
    elif(computer == 0 and you == -1):
        print("You win!!")

    else:
        print("Something went wrong!!")

    
