##### The Spell Class   #####
class Spell():
    """The base class for all items"""

    def __init__(self, name, description, effect, cost):
        self.name = name
        self.description = description
        self.effect = effect
        self.cost = cost

    def __str__(self):
        return "{} : {}  //  Effect: {} Mana Cost: {}".format(self.name, self.description, self.effect, self.cost)

