# score_file = open("score.txt","r",encoding ="utf8")
# print(score_file.read())
# score_file.close()
score_file = open("score.txt","r",encoding ="utf8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()