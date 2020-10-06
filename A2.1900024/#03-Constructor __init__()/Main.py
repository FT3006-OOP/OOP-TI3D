class Hero : #template
    
    def __init__(self,inputName,inputHP,inputATK,inputArmor):
        self.name=inputName
        self.HP=inputHP
        self.ATK=inputATK
        self.Armor=inputArmor


hero1 = Hero("Axe",320,10,8)
hero2 = Hero("Antimage",240,12,3)
hero3 = Hero("Udin",99999,500,0)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)