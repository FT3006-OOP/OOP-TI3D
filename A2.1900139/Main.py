class Hero: # template
    pass


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero();

hero.name = "sniper"
hero.health = 100

Hero.name = "sven"
hero.health = 200

hero.name = "ucup"
hero.health = 1000

print(hero1)
print(hero._dict_)
print(hero1.name)