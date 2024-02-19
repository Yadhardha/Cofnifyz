import random
n = int(input("Enter a number:"))
r1 = random.randint(1,100)
if 50 < r1:
    print("Hurray your score is higher")
elif 90 < r1 < 100:
    print("Bravo ur score is awsm ")
else:
    print("Better luck next time ur score is lower")