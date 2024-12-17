
def calculator():
    operator = input("Enter an operator (+, -, *, /): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Error! Invalid operator.")
        return

    print(f"Result: {result}")





