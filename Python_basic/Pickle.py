# import pickle 
# profile_file = open("profile.pickle","wb") # binary
# profile = {"name" : "park" , "age" : 17 , "hobby" : ["soccer","coding","baseball"]}
# print(profile)
# pickle.dump(profile,profile_file)
# profile_file.close()

import pickle 
profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()