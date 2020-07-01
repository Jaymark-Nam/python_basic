#CLASS

class unit:
    def __init__(self,name,hp,damage):  
                                            #__init__ : 마린,탱크같은 객체가 만들어질때 호출되는 생성자
        self.name = name                    #member parameter
        self.hp = hp
        self.damage= damage
        print("{0} unit is created ".format(self.name))
        print("health {0}, damage {1}".format(self.hp, self.damage))


marine1 = unit("Marine", 40, 5)
marine2 = unit("Marine", 40, 5)
tank = unit("Tank",150,54)

race1= unit("Race",80,5)
print("unit name : {0}, damage{1}".format(race1.name, race1.damage))

race2 = unit("Stolen Race",80,5)
race2.clocking = True

if race2.clocking == True:
    print("{0} is clocked mode".format(race2.name))


#Method
class Attackunit :
    def __init__(self,name,hp,damage):  
        self.name = name                   
        self.hp = hp
        self.damage= damage

    def attack(self,location):
        print("{0}: {1} location attack. damage{2}".format(\
            self.name, location, self.damage))  #self means itself. In method u need to write 'self',,, location은 전달받은 값을 씀
    
    def damaged(self, damage):
        print("{0}: {1} location attack. damage{2}".format(\
            self.name, damage))  
        self.hp -= damage
        print("{0} : now hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))

firebat1 = Attackunit("Firebat",50,16)
firebat1.attack("5hour")
firebat1.damaged(25)
firebat1.damaged(25)

