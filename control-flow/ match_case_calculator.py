# A script that implements a simple calculator using match-case statements.

num1 = int(input("Enter first number: ")) # Get the first number from the user
num2 = int(input("Enter second number: ")) # Get the second number from the user

operation = input("Choose the operation (+, -, *, /): ").strip().lower()

# Perform the calculation based on the chosen operation
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    case _:
        result = "Error: Invalid operation."
# print the result
print(f"The result is: {result}")