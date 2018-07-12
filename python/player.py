import item as items


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def isalive(self):
        return self.health

    def addItem(self, item):
        self.inventory.append(item)

    def removeitem(self, item):
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item.name == name:
                self.inventory.pop(i)
                return



    def use(self, name):
        if self.hasitem(name):
            for i in item.items:
                if i.name == name:
                    self.health += i.healing

    def hasItem(self, name):
        for item in self.inventory:
            if item.name == name:
                return True
        return False

        def getItems(self):
            items = []
            for item in self.inventory:
                item.append(item.name)
            return items
