class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print("{1} is going to [floor unit] {0} location".format(location,self.name))

      

class AttackUnit(Unit):
    def __init__(self,name,hp,damage,speed):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
        print("{0} unit is born".format(self.name))
    
    def attack(self,location):
        print("{0} is attck {1} with {2} damage".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} damaged ".format(self.name,damage))
        self.hp -= damage
        if(self.hp <= 0):
            print("{0} is fail".format(self.name))

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} [speed : {2}]".format(name,location,self.flying_speed))


class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage,0)
        Flyable.__init__(self,flying_speed)

    def move(self,location):
        print("[fly unit move]")
        self.fly(self.name,location)



class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass

supply_depot = BuildingUnit("Supplydepot",500,"7")


def game_start():
    print("[notice] game start")

def game_over():
    pass


game_start()
game_over()