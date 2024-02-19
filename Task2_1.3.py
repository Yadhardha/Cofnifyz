def checker(s):
    lo = 0
    up = 0
    sp = 0
    d = 0
    for i in s:

        if i.isupper() == True:
            up += 1

        elif i.islower() == True:
            lo += 1

        elif i.isdigit() == True:
            d += 1
        else:
            sp += 1
    if len(s) >= 6 and up >= 1 or sp > 1 or lo > 5:
        return "Strong Password"
    else:
        return "Enter strong password"


s = input("Enter password:")
print(checker(s))
