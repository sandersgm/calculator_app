import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error: Cannot take square root of a negative number."
    return math.sqrt(x)

def exponentiate(x, y):
    return x ** y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculator():
    print("=== Command Line Calculator ===")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponentiation")

    choice = input("Enter choice (1-6): ")

    if choice == '5':
        num = get_number("Enter a number: ")
        result = square_root(num)
    elif choice in ['1', '2', '3', '4', '6']:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '6':
            result = exponentiate(num1, num2)
    else:
        print("Invalid choice.")
        return

    print("Result:", result)

if __name__ == "__main__":
    calculator()
