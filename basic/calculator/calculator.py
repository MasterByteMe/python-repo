# Python Calculator

operator = input("Enter the operator (* / + -): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "*":
    total = num1 * num2
    print("--------------------")
    print(round(total))
elif operator == "/":
    total = num1 / num2
    print("--------------------")
    print(round(total))
elif operator == "+":
    total = num1 + num2
    print("--------------------")
    print(f"The sum of two numbers is: {total}")
elif operator == "-":
    total = num1 - num2
    print("--------------------")
    print(round(total))
else:
    print("Enter valid operator")
