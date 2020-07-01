#function

def open_account() :        #just made. not operated now
    print("New account is made")

open_account() #finally u can use this function




#pass value, return value
def deposit(balance, money):
    print("You put the money. balance is {0} $ ".format(balance+money))
    return balance+money

def withdraw(balance,money):
    if balance >= money :
        print("You withdrawed the money. balance is {0} $".format(balance-money))
        return balance - money
    else :
        print("U dont have money. money left is {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    comission = money/10
    print("comittion{0}  balance{1}".format(comission,balance-money-comission))
    return comission, balance - money - comission


balance = 0 
balance = deposit(balance, 4000)
print(balance)

balance = withdraw(balance, 1000)
balance = withdraw(balance, 500)

comission, balance = withdraw_night(balance, 500)




#default value
def profile(name,age,main_lang) :
    print("name : {0}, age : {1}, main language : {2}"\
        .format(name,age,main_lang))

profile("Messi",20,"Japanese")
profile("Ronaldo",60,"Thai")




def profile(name,age=16,main_lang="Korean") :
    print("name : {0}, age : {1}, main language : {2}"\
        .format(name,age,main_lang))

profile("Neymar")
profile("Adrianu")



#Keyword value   순서바뀌어도 밑처럼하면돼
def profile(name, age, lang):
    print(name, age, lang)

profile(name="Nani", lang="Viet", age=50)


#changeable
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("name {0}, age {1}".format(name,age))
    print(lang1, lang2, lang3, lang4, lang5)

profile("Xazi",34,"C","C$","C@","C#","C++")
profile("Zidanne",44,"C","C$","","","")


def profile(name, age, *language):
    print("name {0}, age {1}".format(name,age))
    for i in language:
        print(i, end=" ")
    print()
    
profile("Xazi",34,"C","C$","C@","C#","C++", "Java","py")
profile("Zidanne",44,"C")


#local param, global param
gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("(in func)left gun {0}".format(gun))

print("all gun {0}".format(gun))
checkpoint(2)
print("left gun {0}".format(gun))




def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("(in func)left gun {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 3)
print("left gun {0}".format(gun))



#Quiz
def std_weight(height,gender):
    if gender=="male":
        std=str((height/100)*(height/100)*22)
        print("{0}cm {1}'s standard weight is {2} "\
            .format(height,gender,std[0:5]))
        return std[0:5]
    else :
        std=str((height/100)*(height/100)*21)
        print("{0}cm {1}'s standard weight is {2} "\
            .format(height,gender,std[0:5]))
        return std[0:5]

std_weight(184,"male")
std_weight(164,"animal")

# or ... round(std,2)  소수점 2째


    



