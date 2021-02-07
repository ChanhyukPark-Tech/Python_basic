# input = "http://naver.com"
# temp1 = input[7:]
# temp2 = temp1[0:-4]
# temp3 = temp2[:3]
# word_length = len(temp2)
# count = temp2.count("e")

# print(temp3 + str(word_length) + str(count) + "!")

url = "http://naver.com"
my_str = url.replace("http://","")

my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0} password is {1}".format(url , password))