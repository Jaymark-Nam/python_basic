class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class Flyable_Unit(Unit,Flyable):
    def __init__(self):
        # super().__init__()  #다중 상속 시 마지막 부모 클래스만.. 그래서 unit.__init__(self) 로 초기화해야함
        Unit.__init__(self)
        Flyable.__init__(self)

        
dropship = Flyable_Unit()