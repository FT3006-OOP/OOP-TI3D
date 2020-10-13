class Hero : #template
    #Class Variable
    jumlah =0
    def __init__(self,inputName,inputHP,inputATK,inputArmor):
        #InstanceVariable
        self.name=inputName
        self.HP=inputHP
        self.ATK=inputATK
        self.Armor=inputArmor
        Hero.jumlah+=2
        print("Membuat Hero dengan nama " +inputName)


hero1 = Hero("Axe",320,10,8)
print(Hero.jumlah)
hero2 = Hero("Antimage",240,12,3)
print(Hero.jumlah)
hero3 = Hero("Udin",99999,500,0)
print(Hero.jumlah)