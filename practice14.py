#Method Overiding. 자식 클래스 메소드를 쓰고플 때 새로 메소드를 정의하여 사용



class unit:
    def __init__(self, name, hp, velocity):
        self.name = name
        self.hp = hp
        self.velocity = velocity
    
    def move(self, location):
        print("Unit move")
        print("{0} : {1} location. velocity {2}"\
            .format(self.name, location, self.velocity))


class attackunit(unit):     # unit 상속
    def __init__(self, name, hp, velocity, damage):
        unit.__init__(self, name, hp, velocity)   #unit  name, hp 상속
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} location. Damage {2} ".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : now hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))

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


vulture = attackunit("Vulture", 80, 10, 20)
battlecruiser = flyable_attack("BattleCruiser",500,25,3)

vulture.move("Westside")
battlecruiser.fly(battlecruiser.name, "Southsa")
battlecruiser.move("Wessa")




class buildingunit(unit):
    def __init__(self, name, hp, location):
       # pass        : act like its done
       super().__init__(name,hp,0)         # =  unit.__init__(self, name, hp, 0)
       self.location = location


supply_depot = buildingunit("Supply depot", 500, "Northa")


def game_start():
    print("Game starts..")


def game_over():
    pass
