#tuple _ cant modify but faster than list

menu= ("Pork","Chicken")
print(menu[0])
print(menu[1])


name = "Harry"
age = 30
hobby = "coding"
print(name,age,hobby)


#tuple
(nationality,sex,face)=("Brazil","M","good")
print(nationality,sex,face)





#set : 중괄호 .... 중복 no, 순서 무작위
myset = {1,2,3,3,3}
print(myset)

Brazil = {"Neymar","Ganso"}
Argen = set(["Messi","Ganso"])

#교집합 brazil + Argen
print(Brazil & Argen)

#합집합 brazil + Argen
print(Brazil | Argen)

#차집합
print(Brazil-Argen)

# set add, remove
Argen.add("Maradona")
print(Argen)
Argen.remove("Messi")
print(Argen)



#Change of data structure 
menu = {"Coffe","Milk","Juice"}    #set {}
print(menu, type(menu))

menu = list(menu)                  #list []
print(menu, type(menu))

menu = tuple(menu)                 #tuple ()
print(menu, type(menu))


#random + shuffle
from random import *
list = [1,2,3,4,5]
print(list)
shuffle(list)
print(list)
print(sample(list,1))   #랜덤으로 list에서 1개 뽑기



#quiz
#member = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
member = range(1,21)  # 1 to 20
print(type(member))
#member = list(member)

coffee= (sample(member,3))
chicken= (sample(member,1))
print(coffee)
print(chicken)
