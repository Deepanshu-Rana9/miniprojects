# python compound interest calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount can't be less than zero.")
    else:
        break

while True:
    rate = float(input("Enter the Interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero.")
    else:
        break

total = principle * pow((1 + rate/100),time)

print(f"The amount in {time} years is ${total}.")