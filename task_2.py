import random
class Dice:
    def __init__(self, count=1, facets=6, seed=None):
        self.facets = facets
        self.count = count
        self.seed=seed
    def roll(self):
        random.seed(self.seed)
        return [random.randint(1, self.facets) for n in range(self.count)]
d1 = Dice(seed=999)
d2 = Dice(seed=999)
print(d1.roll() ,d2.roll())