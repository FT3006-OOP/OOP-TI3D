class Hero: #template
    #class variabel
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
       
    # void function, method tampa return
    def siapa(self):
        print("namaku adalah" + self.name)

hero1=Hero("sniper", 100, 10, 5)
hero2 = Hero("mario bros", 90, 5,10)

hero1.siapa()
