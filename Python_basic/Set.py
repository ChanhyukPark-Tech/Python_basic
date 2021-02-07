my_set = {1,2,3,3,3}
print(my_set)

java = {"you" , "kim" , "yang"}
python = set(["you","park"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

python.add("kim")
print(python)

java.remove("kim")
print(java)