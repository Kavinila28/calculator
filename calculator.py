
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+ - * /): ")

if op == '+':
    print("Result on window:", a + b)
elif op == '-':
    print("Result on window:", a - b)
elif op == '*':
    print("Result on window:", a * b)
elif op == '/':
    if b != 0:
        print("Result on window:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")
