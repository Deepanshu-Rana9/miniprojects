import random,sys

print("---------Welcome to the Game---------")
print("         ROCK  PAPER  SCISSOR")
wins = 0
loses = 0
ties = 0

while True:
    print('%s Wins, %s Loses, %s Ties'%(wins,loses,ties))
    while True:
        print("Choose your move: (r)ROCK ,(p)PAPER ,(s)SCISSOR and (q)QUIT")
        playermove = input()
        if(playermove=="q"):
            sys.exit()
        elif(playermove=="r" or playermove=="p" or playermove=="s"):
            break

    if(playermove=="r"):
        print("ROCK VERSUS.....")
    elif(playermove=="p"):
        print("PAPER VERSUS.....")
    elif(playermove=="s"):
        print("SCISSOR VERSUS.....")

    computermove = random.randint(1,3)
    if(computermove==1):
        computermove = "r"
    elif(computermove==2):
        computermove ="p"
    elif(computermove==3):
        computermove = "s"

    if(computermove==playermove):
        print(f"comupter chooses {computermove}")
        print("Its a Tie.")
        ties+=1
    elif(computermove=="r" and playermove=="p"):
        print("Computer Choose ROCK.")
        print("YOU WIN.")
        wins+=1
    elif(computermove=="r" and playermove=="s"):
        print("Computer Choose ROCK.")
        print("YOU LOSE.")
        loses+=1
    elif(computermove=="p" and playermove=="r"):
        print("Computer Choose PAPER.")
        print("YOU LOSE.")
        loses+=1
    elif(computermove=="p" and playermove=="s"):
        print("Computer Choose PAPER.")
        print("YOU WIN.")
        wins+=1
    elif(computermove=="s" and playermove=="r"):
        print("Computer Choose SCISSOR.")
        print("YOU WIN.")
        wins+=1
    elif(computermove=="s" and playermove=="p"):
        print("Computer Choose SCISSOR.")
        print("YOU LOSE.")
        loses+=1
