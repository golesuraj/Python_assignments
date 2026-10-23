num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ").strip()
num2 = float(input("Enter second number: "))
match op:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")
