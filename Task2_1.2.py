import random
n = int(input("Enter a number:"))
r1 = random.randint(1, 100)
if 10 < n > r1:
    print("too low")

elif n > r1:
    print("Too high")
elif n == r1:
    print('Matched hurray')
