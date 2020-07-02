
from random import *

class unit:
    def __init__(self, name, hp, velocity):
        self.name = name
        self.hp = hp
        self.velocity = velocity
        print("{0} unit is created".format(name))

    def move(self, location):
        print("Unit move")
        print("{0} : {1} location. velocity {2}"\
            .format(self.name, location, self.velocity))
    
    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : now hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))


class attackunit(unit):     # unit 상속
    def __init__(self, name, hp, velocity, damage):
        unit.__init__(self, name, hp, velocity)   #unit  name, hp 상속
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} location. Damage {2} ".format(self.name, location, self.damage))
    
class marine(attackunit):
    def __init__(self):
        attackunit.__init__(self,"Marine",40,1,5)
    def steampack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} used Steam pack. hp 10 minus".format(self.name))
        else :
            print("{0} : cant use Steam pack".format(self.name))

class tank(attackunit):
    seize_developed = False 

    def __init__(self):
        attackunit.__init__(self,"Tank",150,1,35)
        self.seize_mode = False

    def seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : Seize mode".format(self.name))
            self.damage *=2
            self.seize_mode = True
        else : #seize mode deactivate
            print("{0} : Seize mode deact".format(self.name))
            self.damage /= 2
            self.seize_mode = False

        

class flyable:
    def __init__(self, speed):
        self.speed = speed
    def fly(self, name, location):
        print("{0} : flying to {1}, speed {2}".format(name, location, self.speed))

class flyable_attack(attackunit, flyable):   #have 2 parents
    def __init__(self, name, hp, damage, speed):
        attackunit.__init__(self, name,hp,0,damage) #velocity = 0
        flyable.__init__(self, speed) 

    def move(self, location):
        print("fly unit move")
        self.fly(self.name, location)

class Race(flyable_attack):
    def __init__(self):
        flyable_attack.__init__(self, "Race",80,20,5)
        self.clocked = False 
    
    def clocking(self):
        if self.clocked == True :
            print("{0}: Deact clocking mode")
            self.clocked = False
        else :
            print("{0}: Act clocking mode")
            self.clocked = True

def game_start():
    print("New game starts ")

def game_over():
    print("Player got out of game.")



game_start()

m1 = marine()
m2 = marine()
m3 = marine()
t1= tank()
t2= tank()
r1=Race()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(r1)

for unit in attack_units:
    unit.move("30,50")

tank.seize_developed= True
print("Tank seize mode is developed")


for unit in attack_units:
    if isinstance(unit,marine) :
        unit.steampack()
    elif isinstance(unit, tank) :
        unit.seize_mode()
    elif isinstance(unit,Race):
        unit.clocking()


for unit in attack_units:
    unit.attack("20,50")

for unit in attack_units:
    unit.damaged(randint(5,21))

game_over()







