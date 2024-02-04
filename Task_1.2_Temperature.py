temp = float(input("Enter temperature:"))
unit = input("Enter unit:")
if unit == "C" or "c":
    ct = (temp * 9 / 5) + 32
    print("Celsius in temperature = ", ct)
elif unit == "F" or "f":
    ct = (temp - 32) * 5 / 9
    print("Fahrenheit in temperature = ", ct)
else:
    pass
