from random import *
print(random())  #0<=  <1 random 
print(random()*10)  #0<=  <10 random
print(int(random()*10))  #0<=  <10 int 
print(int(random()*10)+1)  #1<=  <11 int 
print(int(random()*10))  #0<=  <10 int 

#lotto 
print(int(random()*45) +1)
print(randrange(1,46))    # 1<= <46
print(randint(1,45))     #1<= <=45



date = randint(4,31)
print("Offline study meeting is every month"+str(date))
