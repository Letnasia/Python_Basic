while True:
    x = float(input("Enter a number: "))
    y = float(input("Enter a number: "))
    z = input("Enter the operator for these numbers: ")
    if z == '+':
        print(x + y)
    elif z == '-':
        print(x - y)
    elif z == '*':
        print(x * y)
    elif z == '/':
        if y != 0:
            print(x / y)
        else:
            print("Error. The divisor can't be 0.")
    else:
        print("Error. Unknown operator.")

    continue_cal = input("Do you want to continue? Print 'y' or 'yes' if yes. ")

    if continue_cal != 'y' and continue_cal != 'yes':
        print("The end.")
        break
