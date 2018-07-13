import random
import sys
import time
import player
import location
import item
import enemy
from datetime import datetime
print ("What game do you want to play?")
time.sleep(1)
print("do you want to play wildernessexplorer or dungeoncrawler?")
#print("wildernessexplorer/dungeoncrawler>").lower() == "wildernessexplorer"
print("You will play Wilderness Explorer")
time.sleep(2)

seed = input("enter a seed: ")

tile = location.Location(seed + "0, 0")

user = player.Player(input("What is your name: "))

x = 0
y = 0
tiles = {}
searched_tiles = []

def move(direction):
    global x, y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "s":
        y -= 1
    elif direction == "w":
        x -= 1
    key = "{},{}".format(x, y)
    if key in tiles:
        return tiles[key]
    else:
        newtile = location.Location(seed + key)
        tiles[key] = newtile
        return newtile

running = True
while running and user.isalive():
    print("You are in {}".format(tile.name))
    if tile.enemy and tile.enemy.isAlive():
        print("There is an enemy present! They have {} health.".format(tile.enemy.health))
    command = input("> ")
    if command == "items":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("Moving cancelled")
    elif command == "search":
        if tile.seed in searched_tiles:
            print("You already searched here.")
            continue
        random.seed(seed + str(x) + str(y))
        if random.randint(1, 2) == 1:
            print("You seem to have found something")
            user.addItem(item.getRandomItem())
        else:
            print("You search for a while but find nothing")
            searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())
        while tile.enemy.isAlive():
            print("You have {} health!".format(user.health))
            command = input("FIGHT MODE >")
            if command == "punch":
                if random.randint(1, 5) < 5:
                    print("You punched the enemy")
                    tile.enemy.health -= 3
                else:
                    print("You are clumsy and missed your hit! oof.png")
            elif command == "curbstomp":
                if random.randint(1, 5) == 1:
                    print("WOW a succesful curbstomp!")
                else:
                    print("What a horrid attempt")
                    if tile.enemy.health > 0:
                        user.health -= tile.enemy.damage
                    elif command.startswith("heal"):
                        _, item = command.split(" ", 1)
                        if user.hasitem("life cereal"):
                            print("You have eaten the whole box. DRY.")
                            user.health += 10
                            user.removeitem("life cereal")
                        else:
                            print("You have no healing items")
    elif command == "move":
        direction = input("N/E/S/W > ")[0].lower()
        if direction == "n":
            tile = move("n")
            print("Go north")

        elif direction == "e":
            tile = move("e")
            print("Go east")

        elif direction == "s":
            tile = move("s")
            print("Go south")

        elif direction == "w":
            tile = move("w")
            print("Go west")

        else:
            print("no")



else:
    name = input("A lone hero wanders a dungeon... What is their name? ")
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
