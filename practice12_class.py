
#pickle : save data into file type
import pickle 
profile_file = open("profile.pickle","wb") # making a file/ w=writing/  b= binary, for using pickle b is essential
profile = {"name":"Park", "age":34, "hobby":["football","golf","game"]}
print(profile)
pickle.dump(profile, profile_file)  #save 'profile' data into profile_file
profile_file.close()

#data 불러오기
profile_file = open("profile.pickle","rb") 
profile = pickle.load(profile_file)  #bringing file to profile
print(profile)
profile_file.close()



#with : no need to close file
import pickle
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

#with_writin
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("I'm working hard on python")

#with_read
with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())


#quiz
for i in range(1,51):
    with open("{0}week.txt".format(i),"w") as week_file:
        week_file.write("{0}week summary".format(i))
        week_file.write("\nDepartment: \nName: \nSummary:")




#CLASS : important
name = "Suno"
hp = 80
damage = 10
print("{} Unit has been created".format(name))
print("hp{0}, damage{1}".format(hp, damage))


tank_name = "tank"
tank_hp = 150
tank_damage = 45
print("{} Unit has been created".format(tank_name))
print("hp{0}, damage{1}".format(tank_hp, tank_damage))



tank2_name = "tank"
tank2_hp = 150
tank2_damage = 45
print("{} Unit has been created".format(tank2_name))
print("hp{0}, damage{1}".format(tank2_hp, tank2_damage))




def attack(name, location, damage):
    print("{0} : attack in {1} location, damage{2}".format(\
        name, location, damage))

attack(name, "1hour",damage)
attack(tank_name, "1hour", tank_damage)
attack(tank2_name, "1hour", tank2_damage)