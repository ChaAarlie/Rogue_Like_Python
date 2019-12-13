from Items import *


#########        THIS CLASS IS USELESS          #########
#
class Inventory():
    def __init__(self):
        self.items = []

    def god_inventory(self):
        filepath = 'items.txt'
        file = open(filepath, "r")
        for line in file:
            split = line.split(";")
            if split[0] == "Weapon":
                self.add_item(Weapon(split[1], split[2], int(split[3]), int(split[4])))
            if split[0] == "Armor":
                self.add_item(Armor(split[1], split[2], int(split[3]), int(split[4])))
            if split[0] == "Jewel":
                self.add_item(Jewel(split[1], split[2], int(split[3]), split[4]))
            if split[0] == "Consumable":
                self.add_item(Consumable(split[1], split[2], int(split[3]), split[3]))
        file.close()



    def add_item(self, item):
        self.items.append(item)