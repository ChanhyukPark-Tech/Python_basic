from random import *

# custom_want = randint(5,50)

# while i <= 50:
#     customer[i] = custom_want
#     print("{0} customer time is (time : {1}".format(i,customer.get(i)))

cnt = 0 
for i in range(1,51): # 1~50 NUMBER 
    time = randrange(5, 51) # 5 minute ~ 50 minute~
    if 5<= time and time <=15:
        print("[O] {0} customer (time : {1} minute)".format(i,time))
        cnt += 1
    else:  # matching fail
        print("[ ] {0} customer (time : {1} minute)".format(i,time))
        
print("total : {0}".format(cnt))
