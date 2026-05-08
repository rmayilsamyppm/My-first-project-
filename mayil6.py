import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Invalid input"
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        return "Invalid input"
    return math.factorial(n)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", divide(a, b))

    elif choice == 5:
        a = float(input("Enter base number: "))
        b = float(input("Enter exponent: "))
        print("Result:", power(a, b))

    elif choice == 6:
        a = float(input("Enter number: "))
        print("Result:", square_root(a))

    elif choice == 7:
        n = int(input("Enter integer: "))
        print("Result:", factorial(n))

    elif choice == 8:
        x = float(input("Enter angle in degrees: "))
        print("Result:", sine(x))

    elif choice == 9:
        x = float(input("Enter angle in degrees: "))
        print("Result:", cosine(x))

    elif choice == 10:
        x = float(input("Enter angle in degrees: "))
        print("Result:", tangent(x))

    elif choice == 11:
        print("Calculator Closed")
        break

    else:
        print("Invalid choice")
