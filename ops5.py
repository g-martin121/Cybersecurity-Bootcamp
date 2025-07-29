number1= int(input("Enter a number:"))
number2= int(input("Enter a number:"))
operation= (input("Choose an operation (+, -, *, /):"))

if operation == "+":
    result = number1 + number2
    print(result)
elif operation == "-":
    result = number1 - number2
    print(result)
elif operation == "*":
    result = number1 * number2
    print(result)
elif operation == "/":
    result = number1 / number2
    print(result)
    if number2 == 0:
        print("Invaild")
