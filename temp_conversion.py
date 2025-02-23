# Temperature conversion

temp = float(input("Enter the temperature: "))
unit = input("Enter your unit in fahrenheit or celsius (F or C): ")

if unit == "F":
    temp = (temp * 9/5) + 32
    unit = "°F"
    print(f"The temperature in fahrenheit is {round(temp,2)}{unit}")
elif unit == "C":
    temp = (temp - 32) * 5/9
    unit = "°C"
    print(f"The temperature in celsius is {round(temp,2)}{unit}")
else:
    print(f"{unit} is not a valid unit!")


