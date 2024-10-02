operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid Operator Entered!")