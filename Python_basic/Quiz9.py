class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    print("[remain chicken : {0}".format(chicken))
    try:
        order = int(input("how much you want to chicken?"))
        
        if order > chicken :
            print("Sold out you cannot eat")
        elif order < 1 :
            raise ValueError
        else:
            print("[waiting {0}] {1} chicken is ok !".format(waiting , chicken))
            waiting += 1 
            chicken -= order     
        if chicken == 0 :
            raise SoldOutError
    except ValueError:
        print("plz put in proper value")
    except SoldOutError as err:
        print(err)
        print("sorry sold out")
        break