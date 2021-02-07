try:
    print("dividble calculator")
    num1 = int(input("Type your first number : "))
    num2 = int(input("Type your second number : "))
    print("{0} / {1} = {2} ".format(num1 , num2 , int(num1 / num2)))
except ValueError:
    print("Error ! wrong value! ")
except ZeroDivisionError as err:
    print(err) 