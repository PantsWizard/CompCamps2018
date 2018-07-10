class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def addItem(self, item):
        self.inventory.append(item)

    def hasItem(self, name):
        for item in self.inventory:
            if item.name == name:
                return True
        return False

        def getItems(self):
            items = []
            for item in self.inventory
                item.append(item.name)
            return itemssa
