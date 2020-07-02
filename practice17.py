
class Soldouterror(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try :
        print("Left chicken {0}".format(chicken))
        order = int(input("How many chicken do you want"))
        if order > chicken:
            print("No chicken")
        elif order <= 0:
            raise ValueError
        else :
            print("Waiting num {0}. {1}chickens order ok"\
                .format(waiting,order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise Soldouterror

    except ValueError :
        print("Error")
    except Soldouterror:
        print("No chicken left!!!")
        break




'''
#Error occur

class bignumbererror(Exception):   #user define error 
    def __init__(self,mfg):
        self.msg = msg

    def __str__(self):
        return self.msg
try :
    print("한자리 숫자 나누기 계산기")
    num1 = int(input("num1"))
    num2 = int(input("num2"))
    if num1 >=10 or num2 >=10:
        raise bignumbererror("{0}{1}".format(num1,num2))
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("Error")
except bignumbererror as err:
    print("Error occured. only one number")
    print(err)
finally :
    print("Thanks for using calculator")
    '''