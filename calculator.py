# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b

while True:
    print("\n===== Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Choose option (1-5): ")

    if choice == '5':
        print("Bye bye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Answer:", add(num1, num2))
        elif choice == '2':
            print("Answer:", subtract(num1, num2))
        elif choice == '3':
            print("Answer:", multiply(num1, num2))
        elif choice == '4':
            print("Answer:", divide(num1, num2))
    else:
        print("Wrong choice! Try again.")