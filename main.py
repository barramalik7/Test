import re

# Welcome message
print("Welcome to the calculator program")

while True:
    # prompt user for input
    Soal = input("Enter your calculation: ")

    # extract operator and operands using regular expressions
    pattern = r"(\d+)\s*([-+*/])\s*(\d+)"
    match = re.match(pattern, Soal)

    if match:
        num1 = float(match.group(1))
        operator = match.group(2)
        num2 = float(match.group(3))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid operator")

        print("Result: ", result)

        response = input("Do you want to continue? (y/n): ")
        if response == "y":
            continue
        else:
            print("Thank you for using the calculator program")
            break
    else:
        print("Invalid input. Please enter a valid arithmetic expression.")
        continue
