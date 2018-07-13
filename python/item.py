import random

class Item:
    def __init__(self, name, damage, healing):
        self.name = name
        self.damage = damage
        self.healing = healing

items = [
    Item("life cereal", 0, 10),
    Item("stick", 1, 0),
    Item("really long popsicle", 2, 5),
]

def getRandomItem():
    return item(random.choice(items))
