def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user
    operation = input("Enter choice (1/2/3/4): ")

    # Input validation
    if operation not in ['1', '2', '3', '4']:
        print("Invalid input. Please select a valid operation.")
        return

    # Input numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # Perform the corresponding operation
    if operation == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    calculator()
