class Hero:

    #private class variabel
    __jumlah = 0

    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__lavel = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__lavel
        self.__attPower = self.__attPowerStandar * self.__lavel
        self.__armor = self.__armorStandar * self.__lavel

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name,self.__lavel,self.__health,self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'lavel up')
            self.__lavel += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__lavel
            self.__attPower = self.__attPowerStandar * self.__lavel
            self.__armor = self.__armorStandar * self.__lavel

    def attack(self,musuh):
        self.gainExp = 50

slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)
