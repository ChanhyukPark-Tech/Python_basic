from random import *


# normal unit
class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} unit was born.".format(self.name))

    def move(self,location):
        print("[Floor Unit Movement]")
        print("{0} : {1} direction moving now . [SPEED : {2} ".format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0} : {1} damaged".format(self.name,damage))
        self.hp -= damage
        print("{0} : now hp is {1}".format(self.name,self.hp))
        if(self.hp <= 0):
            print("{0} : die ".format(self.name))

# Attack Unit

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} direction attack [Attack Damage {2}]".format(self.name,location,self.damage))

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("Marine",40,1,5)

    # skill
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Use StimPack ! (HP - 10) ! ".format(self.name))
        else:
            print("{0} : Can not use StimPack cuz hp is not sufficient".format(self.name))


class Tank(AttackUnit):

    seize_developed = False

    def __init__(self):
        super().__init__("Tank",150,1,35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False :
            return
        
        if self.seize_mode == False:
            print("{0} : do seize mode ! upgrade damage ! ".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : not seize mode ! downgrade damage ! ".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} direction flying now ! . [SPEED : {2}]".format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,flying_speed)
    
    def move(self,location):
        print("[FlyingUnit Moving now]")
        self.fly(self.name,location)


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"wraith",80,20,5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : down Clocking mode bye bye ".format(self.name))
            self.clocked = False
        else:
            print("{0} : use Clocking mode you can not see me".format(self.name))
            self.clocked = True

def game_start():
    print("[notice] new game!")

def game_over():
    print("Player : gg") # good _ game
    print("[Player] was out from game" )




### real game from now

game_start()
#three marine

m1 = Marine()
m2 = Marine()
m3 = Marine()

#tank 2 

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#move all ! 

for unit in attack_units:
    unit.move("1oclock")

Tank.seize_developed = True
print("[notice] tank can use seize mode from now")

#attack prepare
# this point is important
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    else :
        unit.clocking()                                     

# Attack!!!!

for unit in attack_units:
    unit.attack("1'oclock!")

# damaged
    for unit in attack_units:
         unit.damaged(randint(5,20))       # 5~20

game_over()