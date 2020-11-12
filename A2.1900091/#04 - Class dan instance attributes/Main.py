class Hero: #template
    #class variabel
    jumlah = 0

    def _init_(self, inputName, inputHealth, inputPower, inputArmor):
        # onstance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("membuat Hero dengan nama" + inputName)


hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("mirana", 100, 15,1)
print(Hero.jumlah)
Hero3 = Hero("ucup", 1000, 100, 0)


