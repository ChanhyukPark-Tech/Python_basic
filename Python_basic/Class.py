class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit is born".format(self.name))
        print("hp {0} and damage is {1}".format(self.hp,self.damage))


wraith1 = Unit("wraith",80,5)
print("Unit name  : {0} , damage : {1} ".format(wraith1.name , wraith1.damage) )