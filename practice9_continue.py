#continue and break

absent = [2,5]
no_book = [7]
for student in range(1,11):  #1-10
    if student in absent:
        continue            #becuz he's absent, continue
    elif student in no_book:
        print("no class, {0} follow me".format(student))
        break               #shut down errthing!
    print("{0}, read that book".format(student))


#one sentence FOR
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)


friend = ["Black belt","Lincoln","Michael Jackson","Tona"]
friend = [len(i) for i in friend]
print(friend)

friend = ["Black belt","Lincoln","Michael Jackson","Tona"]
friend = [i.upper() for i in friend]
print(friend)




#Quiz
# [0] 36 customer.  Spent time 14min
#  total customer : 15 people

from random import *
count = 0 #total customer number
for i in range(1,51):
    time = randrange(5,51)  #5min-50min 
    if 5<= time <=15:
        print("[0] {0} customer.  Spent time {1}min".format(i, time))
        count +=1
    else:
        print("[ ] {0} customer.  Spent time {1}min".format(i, time))

print("total customer : {0} people" .format(count))

        

