
try:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    a = num1/num2
except ZeroDivisionError:
    print("Error:Division by zero is not allowed")
except ValueError:
    print("Please enter numeric values")
else:
    print(a)