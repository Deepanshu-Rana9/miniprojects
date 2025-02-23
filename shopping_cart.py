# shopping cart program

items = []
prices = []
total = 0

while True:
    food = input("Enter a item to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: ₹"))
        items.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in items:
    print(food)

for price in prices:
    total += price

print(f"Your total price is ₹{total}")