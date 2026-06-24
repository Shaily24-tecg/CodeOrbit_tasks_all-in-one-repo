# Simple Calculator Program
# Supports +, -, *, / operations with input validation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

print("=== SIMPLE CALCULATOR ===")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation: +  -  *  /")
    op = input("Enter operator: ")

    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", subtract(num1, num2))
    elif op == "*":
        print("Result:", multiply(num1, num2))
    elif op == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operator selected")

except ValueError:
    print("Error: Please enter valid numeric inputs")