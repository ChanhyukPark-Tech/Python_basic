from random import *


# people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(people)
# chicken = sample(people,1)
# del people[chicken]

# # coffee = sample(people,3)

# # print(chicken , coffee)


users = range(1,21)
users = list(users)
# print(type(users))
shuffle(users)
print(users)

winners = sample(users , 4)

print(" ---- con ----")
print("chicken : {0}".format(winners[0]))
print("coffee : {0}".format(winners[1:]))



