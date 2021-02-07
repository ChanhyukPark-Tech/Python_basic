class Unit:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
      

class AttackUnit(Unit):
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)
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
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)


# balkiri 
valkyrie = FlyableAttackUnit("valkyrie",200,6,5)
valkyrie.fly(valkyrie.name,"3")





# firebat1 = AttackUnit("firebat",50,16)
# firebat1.attack("1")

# firebat1.damaged(25)
# firebat1.damaged(25)