
# list[]

subway = [10,20,30]
print(subway)

subway = ["Zidanne", "Ronaldo", "Essi"]
print(subway)

print(subway.index("Essi")) #which subway is Essi in?

subway.append("Xavi")
print(subway)

subway.insert(1, "Iniesta")     #put him in place 1
print(subway)

subway.append("Zidanne")
print(subway.count("Zidanne"))


#array
num_list = [5,2,4,1,3]
num_list.sort()
print(num_list)     #1,2,3,4,5,

num_list.reverse()
print(num_list)     #5,4,3,2,1

#num_list.clear()
#print(num_list)     #clr



mix_list= ["Xavi", 20, False]
print(mix_list)

num_list.extend(mix_list)
print(num_list)




#dictionary
cabinet = {3:"Potter", 100:"Rohn"} #key :3, value: Potter
print(cabinet[3])
print(cabinet.get(3))
print(cabinet[100])

print(cabinet.get(5, "You can use this key"))

print(3 in cabinet) #True
print(6 in cabinet) #False



cabinet = {"A-3" :"Potter", "B-100":"Rohn"} 
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet)

#new
cabinet["A-3"] = "Hermione"
cabinet["C-20"] = "Hagrid"
print(cabinet)

#gone
del cabinet["A-3"]
print(cabinet)

#only key
print(cabinet.keys())

#only value 
print(cabinet.values())

#both
print(cabinet.items())

#clr
cabinet.clear()
print(cabinet)