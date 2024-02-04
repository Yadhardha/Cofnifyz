def strReversal(s):
    k = ""
    for i in range(len(s) - 1, -1, -1):
        k = k + s[i]

    return k


s = input("Enter a string:")
res = strReversal(s)
print(res)
