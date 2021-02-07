# weather = input("hows the weather")

# if weather == "rain" or weather == "snow" :
#     print("You have to have umbrella")
# elif weather == "bad" :
#     print("You have to have mask")
# else:
#     print("Nothig")


temp = int(input("Type your temperature"))

if(temp > 30 ) :
    print("So hot don't go outside")
elif(temp > 10 & temp <= 30):
    print("Good weather")
elif(temp <= 10 & temp > 0 ):
    print("you have to outer")
else : 
    print("very cold outside")