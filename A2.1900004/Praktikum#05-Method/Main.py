class Hero:
    #class Variabel
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    #void function,method tanpa return
    def siapa(self):
        print("namaku adalah "+self.name)

    #method dengan argumen
    def healthUp(self,Up):
        self.health += Up
        
    #method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Snipper",100,10,4)
hero2 = Hero("Mario Bross",90,5,10)

hero1.siapa()
hero1.healthUp(10)

=======
class Hero:
    #class Variabel
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    #void function,method tanpa return
    def siapa(self):
        print("namaku adalah "+self.name)

    #method dengan argumen
    def healthUp(self,Up):
        self.health += Up
        
    #method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Snipper",100,10,4)
hero2 = Hero("Mario Bross",90,5,10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHealth())