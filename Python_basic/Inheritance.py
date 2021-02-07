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

firebat1 = AttackUnit("firebat",50,16)
firebat1.attack("1")

firebat1.damaged(25)
firebat1.damaged(25)