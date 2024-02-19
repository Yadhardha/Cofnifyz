n = int(input("Enter an integer:"))
a = 0
b = 1
i = 0
print(a)
print(b)
while i <= n:
    a, b = b, a + b
    i += 1
    if b <= n:
        print(b)
