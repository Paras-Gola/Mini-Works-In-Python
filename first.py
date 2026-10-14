try:
    num = float(input("Enter a number: "))
    operator = input("Enter operator (+,-,*,/): ")
    num2 = float(input("Enter another number: "))
    if operator == "+":
        result = num + num2
    elif operator == "-":
        result = num - num2
    elif operator == "*":
        result = num * num2
    elif operator == "/":
        if num2 != 0:
            result = num / num2
        else:
            result = None
        print("Error: cannot divide by zero")
    else:
        result = None
        print("Error: invalid operator")

    if result is not None:
        print("result:",result)

except ValueError:
    print("Error: please enter a Valid number")







