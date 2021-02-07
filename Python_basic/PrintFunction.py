print("i am %d age " % 20)
print("i like %s " % "python")
print("Apple is started by %c" % 'A')

print("i am %s age " % 20)
print("i like %s and %s color" % ("blue" , "red"))

# method 2 
print("i am {}age".format(20))
print("i like {} and {} color".format("blue" , "red"))
print("i like {0} and {1} color".format("blue","red"))
print("i like {1} and {1} color ".format("blue","red"))


#method 3 
print("i am {age} and i like {color}".format(age = 20 , color = "Red"))

#method 4 
age = 20
color = "blue"

print(f"i am {age} and i like {color}")