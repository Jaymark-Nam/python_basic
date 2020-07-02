#상속

class unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class attackunit(unit):     # unit 상속
    def __init__(self, name, hp, damage):
        unit.__init__(self, name, hp)   #unit  name, hp 상속
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} location. Damage {2} ".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0} : {1} damaged".format(self.name, damage))
        self.hp -= damage
        print("{0} : now hp is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed".format(self.name))

firebat1 = attackunit("Firebat",50, 16)
firebat1.attack("East")

firebat1.damaged(25)
firebat1.damaged(25)

#multi herit  : many parents
class flyable:
    def __init__(self, speed):
        self.speed = speed
    def fly(self, name, location):
        print("{0} : flying to {1}, speed {2}".format(name, location, self.speed))

class flyable_attack(attackunit, flyable):   #have 2 parents
    def __init__(self, name, hp, damage, speed):
        attackunit.__init__(self, name,hp,damage) #attackunit 초기화
        flyable.__init__(self, speed) 

valkyrie = flyable_attack("Valkyrie", 200, 30, 5)
valkyrie.fly(valkyrie.name, "Eastwest")


#Method Overiding. 자식 클래스 메소드를 쓰고플 때 새로 메소드를 정의하여 사용




