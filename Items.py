class Item():
    """The base class for all items"""

    def __init__(self, name, description, price, something):
        self.name = name
        self.description = description
        self.price = price


class Weapon(Item):
    def __init__(self, name, description, price, damage):
        self.name = name
        self.description = description
        self.price = price
        self.damage = damage

    def __str__(self):   #to string method used in most classes it's usefull
        return "{} : {}  //  Price: {} Damage: {}".format(self.name, self.description, self.price, self.damage)

class Armor(Item):
    def __init__(self, name, description, price, armor):
        self.name = name
        self.description = description
        self.price = price
        self.armor = armor

    def __str__(self):
        return "{} : {}  //  Price: {} Armor: {}".format(self.name, self.description, self.price, self.armor)

class Jewel(Item):
    def __init__(self, name, description, price, bonus):
        self.name = name
        self.description = description
        self.price = price
        self.bonus = bonus

    def __str__(self):
        return "{} : {}  //  Price: {} Bonus: {}".format(self.name, self.description, self.price, self.bonus)

class Consumable(Item):
    def __init__(self, name, description, price, boost):
        self.name = name
        self.description = description
        self.price = price
        self.boost = boost

    def __str__(self):
        return "{} : {}  //  Price: {} Boost: {}".format(self.name, self.description, self.price, self.boost)