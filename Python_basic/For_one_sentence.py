
#example 1

# students = [5,6,7,8,9]
# print(type(students))
# students = [i+100 for i in students]                < --------- 
# print(students)

#example 2 :

# students = ["Iron man" , "Thor" , "I am Groot"]
# students = [len(i) for i in students]                     < ------------
# print(students)

#exmaple 3:

students = ["Iron man" , "Thor" , "I am Groot"]
students = [i.upper() for i in students]
print(students)