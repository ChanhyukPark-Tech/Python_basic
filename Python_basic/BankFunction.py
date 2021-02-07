

def deposit(balance , money):
    print("deposit is success you balance is {0}".format(balance + money))
    return balance + money

def withdraw(balance , money):
    if(balance > money):     
        print("withdraw is success you balance is {0}".format(balance - money))
        return balance - money
    else:
        print("Cannot withdraw becasue balance is not suffieceint")
        return balance

def withdraw_night(balance, money):
    commission = 100 
    return commission,balance - money - commission

balance = 0 
balance = deposit(balance , 1000)
balance = withdraw(balance, 500)
commission , balance = withdraw_night(balance , 300)
print("commision is {0}  your balance is {1}".format(commission,balance))
