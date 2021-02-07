class BigNumberErro(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg
try:
    print("Only one number")
    num1 = int(input("Type your first number"))
    num2 = int(input("Type your second number"))
    if num1 >=10 or num2 >= 10:
        raise BigNumberErro("input : {0} , {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("Only one number plz")
except BigNumberErro as err:
    print("Error ")
    print(err)
finally:
    print("thank you for using! ")