# simple calculator

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("DIvision: cannot divide by zero")

except ValueError:
    print("invalid input! Please enter number.")