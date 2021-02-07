gun = 10

def checkpoint(soldiers):
    global gun 
    gun = gun - soldiers
    print("remain gun  {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("remain gun {0}".format(gun))
    return gun


gun = checkpoint_ret(gun,2)
print("remain is {0}".format(gun))