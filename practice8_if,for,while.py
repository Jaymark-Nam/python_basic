# IF
weather = input("How is today's weather? : ") #if user enters, the answer comes inside into weather parameter in 'string' 
if weather=="rain" or weather=="snow":
    print("Umbrella needed")
elif weather=="fog":
    print("mask needed")
elif weather=="bad":
    print("So what!")
else :
    print("It's clear man!")



temp = int(input("What's the temperature?"))
if 30 <=temp:
    print("Too hot bro")
elif 10<=temp and temp <30:
    print("pretty good")
elif 0<= temp and temp <10:
    print("bring a coat")
else :
    print("freaking cold")


#FOR

for waiting in [0,1,2,3,4]:
    print("wait {}".format(waiting))


for waiting in range(10): #0-9
    print("wait {}".format(waiting))


for waiting in range(3, 10): #3-9
    print("wait {}".format(waiting))



starbucks = ["Ironman","Thor","Groot"]
for customer in starbucks:
    print("{}, coffee is prepared".format(customer))


#WHILE
vip = "Thor"
call = 5
while call >=1 :
    print("{0},Coffee is prepared. {1} times left".format(vip,call))
    call -=1
    if call==0:
        print("Coffee is gone..")


#vvip = "Spider"
#call_time = 1
#while True:
#    print("{0}, Coffee is finished {1} times called ".format(vvip,call_time))
#
#    call_time += 1


ssum = "Yunsun"
person = ""
while person != ssum:
    print("{0}, coffee is prepared." .format(ssum))
    person = input("What's your name ?")


