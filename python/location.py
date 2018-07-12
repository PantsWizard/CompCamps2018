import random
import enemy

descriptions = ["Hollow", "Quiet", "Whistling", "Mesmerising", "Shrek's"]
location_types = ["Forest", "River", "Cave", "Fields", "Swamp"]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
            )
        self.enemy = enemy.get()
