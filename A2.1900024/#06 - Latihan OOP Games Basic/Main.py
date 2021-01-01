class Hero :
    def __init__(self,name,Health,ATKpower,ArmorNumber):
        self.name = name
        self.health = Health
        self.ATKPower = ATKpower
        self.ArmorNumber= ArmorNumber

    def serang (self,lawan):
        print(self.name + ' menyerang '+ lawan.name)
        lawan.diserang(self,self.ATKPower)

    def diserang(self,lawan,ATKpower_lawan):
        print(self.name +' diserang ' + lawan.name)
        attack_diterima = ATKpower_lawan/self.ArmorNumber
        print('serangan terasa : '+str(attack_diterima))
        self.health-=attack_diterima
        print ('HP ' + self.name + ' tersisa ' + str(self.health))


sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)


sniper.serang(rikimaru)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper)
print('\n')
rikimaru.serang(sniper)