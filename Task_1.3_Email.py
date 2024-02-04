import re


def Email(s):
    pat = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if not re.match(pat, s):
        print("Invalid Email")
    else:
        print("Valid Email")


s = input("Enter an Email:")

Email(s)
