class Hero : #template
    pass


hero1 = Hero() #object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name="Axe"
hero1.health=100

hero2.name="Antimage"
hero2.health=200

hero3.name="Udin"
hero3.health=99999

print(hero1)
print(hero1.__dict__)
print(hero1.name)