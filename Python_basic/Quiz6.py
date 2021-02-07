# def std_weight(height,gender):
#     if(gender == "male"):
#         std_wei = height * height * 22
#     else:
#         std_wei = height * height * 21

#     std_wei = round(std_wei,2)
#     print("height {0} {1} standard weight is {2}".format(height*100,gender,std_wei))


# std_weight(1.75,"male")



def std_weight(height , gender): # height is m <--- float gender is string
    if gender == "male":
        return height * height * 22
    else:
        return height * height * 21


height = 175 # cm 
gender = "male"
weight = round(std_weight(height / 100,gender),2)
print("height {0} gender{1} standard {2}".format(height,gender,weight))