class Hero :
    #Class Variabel
    jumlah_hero = 0
    def __init__(self,inputName,inputHP,inputATK,inputArmor):
        #instance Variabel
        self.name=inputName
        self.HP=inputHP
        self.ATK=inputATK
        self.Armor=inputArmor
        Hero.jumlah_hero += 1

    # void function, method tanpa argumen dan return
    def siapa(self):
        print("Namaku adalah " + self.name)
    # Method dengan argumen, tanpa return
    def ATKUp(self,up):
        self.ATK+=up
    # method dengan return
    def getATK(self):
        return self.ATK


hero1=Hero('Axe',100,10,10)
hero2=Hero('Kevin',100,5,5)


hero1.siapa()
hero1.ATKUp(100)
print(hero1.getATK())