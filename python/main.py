import random
import sys
import time

name = input("A lone hero wanders a dungeon... What is his name? ")
health = 75

score = 0
print

class Dragon:
    """The Final Boss"""
    def __init__(self, name):
        self.name = name
        self.health = 30

    def damage(self):
        return random.randint(1, 10)

    def isalive(self):
        return self.health > 0

    def attack(self):
        damage+random.randint(1,20)
        self.health -= damage
        return damage

class MIT:
    """MITs - The Enemies"""
    def __init__(self, name):
        self.name = name
        self.health = random.randint(10, 20)

    @property
    def damage(self):
        return random.randint(1, 7)

    def isAlive(self):
        return self.health > 0

    def attack(self):
        damage = random.randint(1, 12)
        self.health -= damage
        return damage

mits = [
    MIT("Oversize spider"),
    MIT("Skeleton"),
    MIT("Orc"),
    MIT("Dark mage"),
    MIT("Giant scorpion")
]

random.shuffle(mits)

while len(mits) > 0 and health >0:
    mit = mits.pop()
    print("A savage {} appears!".format(mit.name))
    while mit.isAlive():
        print("You have {} health.".format(health))
        print("the enemy has {} health".format(mit.health))
        print("Do you want to fight or flee?")
        if input("Fight / Flee > ").lower() == "fight":
            damage = mit.attack()
            score += damage
            print("You did {} damage!".format(damage))
            if mit.isAlive():
                damage = mit.damage
                health -= damage
                print("You took {} damage!".format(damage))
                if health <= 0:
                    print("game Over")
                    sys.exit(0)
                else:
                    pass
        else:
            caught = random.randint(1,2) == 1
            if not caught:
                print("You have escaped the dungeon...")
                print("Your score was {}.".format(score))
                sys.exit(0)
            else:
                print("You failed to run away!")
                damage = mit.damage
                health -= mit.damage
                print("You took {} damage!".format(damage))
if health <= 0:
    print("Game Over.")

else:
    print("The hero, {}, has defeated all the monsters in the dungeon...".format(name))
    print("But their worries are not over yet, as you hear a loud booming coming from deep inside the cave...")
    time.sleep(2)
    print("The Dragon guarding the dungeon treasure Has Appeared!")

    dragon = Dragon("Travis")
    while dragon.isalive():
        print("You have {} health".format(health))
        print("The enemy has {} health.".format(dragon.health))
        print("Do you want to Fight or Flee?")
        if input("Fight / Flee > ").lower() == "fight":
            damage = dragon.attack()
            score += damage
            print("You did {} damage.".format(damage))
            if dragon.isalive():
                damage = dragon.damage()
                health -= damage
                print("You took {} damage.".format(damage))
            else:
                caught = random.randint(1, 2) == 1
                if not caught:
                    print("You have defeated the Dragon.")
                    print("Your score is {}".format(score))
                    sys.exit(0)
                else:
                    print("You failed to run away!")
                    damage = dragon.damage
                    health -= dragon.damage
                    print("You took {} damage.".format(damage))



print("Your Score: {}".format(score))
