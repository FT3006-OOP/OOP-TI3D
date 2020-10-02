class Hero: # template
    pass 


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero();


hero1.name = "sniper" #tambahkan =
hero1.health = 100

hero2.name = "sven" #tambahakan =
hero2.health = 200

hero3.name = "ucup" #tambahkan =
hero3.health = 1000

print(hero1)
print(hero1.__dict__) #_dict_
print(hero1.name)