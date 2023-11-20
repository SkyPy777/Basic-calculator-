
# Simple calculator program

# Asking the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Checking for division by zero
if num2 != 0:
    division = num1 / num2
    print(f"Division: {division}")
else:
    print("Cannot divide by zero.")

# Printing the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")

