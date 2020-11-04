class Hero:
    #class variable
    jumlah=0
    __privateJumlah=0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        #instance variable private
        self.__private="private"

        #instance variable protected
        self._protected="protected"

linda=Hero("linda","100")
print(linda.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah)