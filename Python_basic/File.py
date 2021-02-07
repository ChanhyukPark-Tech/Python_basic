# score_file = open("score.txt","w",encoding = "utf8")
# print("math : 0 " , file=score_file)
# print("english : 100 " , file=score_file)

# score_file.close()

score_file = open("score.txt","a",encoding = "utf8") # append
score_file.write("science : 80\n")
score_file.write("coding : 100")
score_file.close()
