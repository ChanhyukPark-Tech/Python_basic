# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

#     #auto close


# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("i studying python")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())