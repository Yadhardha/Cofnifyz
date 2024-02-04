def calculator(a, b, choice):
    if choice == 1:
        print("Addition = ", a + b)
    elif choice == 2:
        print("Subtraction = ", a - b)
    elif choice == 3:
        print("Multiplication = ", a * b)
    elif choice == 4:
        print("Division = ", a / b)
    elif choice == 5:
        print("Modular Division = ", a % b)
    else:
        print("Invalid choice")


a = int(input("Enter an integer:"))
b = int(input("Enter an integer:"))
choice = int(input("Enter an integer:"))
calculator(a, b, choice)
