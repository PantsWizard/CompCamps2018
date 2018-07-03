import random
import sys

name = input("Who dares challenge the MITs? ")
health = 40
score = 0

class MIT:
    """MITs - The Enemies"""
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.damage= random.randint(1,5)
    def damage(self):
        return random.randiant

        @property
        def damage(self):
            return random.randint(1, 7)

        def isAlive(self):
            return self.health > 0

    def attack(self):
        damage = random.randint(0, 10)
        self.health -= damage
        return damage

mits = [
    MIT("Kaitlyn"),
    MIT("Bennet"),
    MIT("Travis"),
    MIT("Rhiannon"),
    MIT("Austin")
]

random.shuffle(mits)


while len(mits)  > 0:
    mit = mits.pop()
    print("A wild {} appears!".format(mit.name))
    while mit.isAlive():
        print("you have {} health." .format(health))
        print("Do you want to fight of flee?")
        if input("Fight / Flee > ").lower() == "fight":
            damage = mit.attack()
            score += damage
            print ("You did{} damage!" .format(damage))
            if mit.isalive():
                damage -= mit.damage
                health =- damage
                print("You ")
        else:
            caught = random.randint(1,5) == 1
            if not caught:
                print ("You have escaped!")
                print("your score was {}".format(score))
                sys.exit(0)
            else:
                print("You failed to run away!")
print ("WOW! You have done it!")
print ("Good job, {}!" .format(name))
print("The MITs have been removed from CompCamps!")
print ("Your score is {}." .format(score))
