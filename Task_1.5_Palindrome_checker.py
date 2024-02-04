def PalindromeChecker(s):
    k = s[::-1]
    if k == s:
        print("{} is a palindrome".format(s))
    else:
        print("{} is not a palindrome".format(s))


s = input("Enter string:")
PalindromeChecker(s)
