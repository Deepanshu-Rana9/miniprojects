questions = ("How many dots appear on a pair of dice?: ",
             "Which country has the highest life expectancy?: ",
             "What phone company produced the 3310?: ",
             "Which planet in the milky way galaxy is the hottest?: ",
             "Kratos is the main character of what video game series?: ")

options = (("A. 34","B. 44","C. 40","D. 42"),
           ("A. Australia","B. Honk Kong","C. India","D. China"),
           ("A. Samsung","B. Nokia","C. Apple","D. Redmi"),
           ("A. Mercury","B. Venus","C. Jupiter","D. Pluto"),
           ("A. GTA 5","B. Summertime Saga","C. God Of War","D. PUBG"))

answers = ("D","B","B","B","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score +=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("---------------------")
print("       RESULT        ")
print("---------------------")

print("Answer: ",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) *100)
print(f"Your score is {score}%")