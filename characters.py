from random import *

from Items import *
from Map import *
from inventory import *

#UPDATE
# contains all the objects of the game
# so the .txt file is open only once
inv = Inventory()
inv.god_inventory()

#TODO achievment, stats
class Player():
    """ This is a class that represents the main character of the game. """

    # (self, name, description, damage, hp, lvl, speed):
    def __init__(self):
        """ This is a method that sets up the variables in the object. """
        self.name = "Link"
        self.sex = "Male"
        self.max_hp = 50
        self.hp = self.max_hp
        self.speed = 20   #decides who attacks first
        self.armor = 0      #reduce damage
        self.parry = 0
        self.crit = 1
        self.max_mana = 100
        self.mana = self.max_mana
        self.damage = 10
        self.lvl = 1
        self.max_xp = 100
        self.xp = 0
        self.parried = False
        self.dodged = False
        self.winner = False
        self.room = 0  # the room the player is in
        self.floor = 0
        self.stage = 0  # (takes value 0,1,2,...) used to know in which stage you are (floors 5-10-15-20-...)
        self.inventory = []
        self.weapon = Weapon
        self.costume = Armor
        self.jewel = Jewel
        self.equiped = [0,0,0]
        self.buffs = []
        self.spells = []
        self.gold = 0

    ################   THE SET METHODES     ############
    def set_name(self, name):
        self.name = name

    def set_speed(self, speed):
        self.speed = speed

    def set_max_hp(self, max_hp):
        self.max_hp = max_hp

    def set_hp(self, hp):
        self.hp = hp

    def set_max_mana(self, max_mana):
        self.max_mana = max_mana

    def set_mana(self, mana):
        self.mana = mana

    def set_damage(self, damage):
        self.damage = damage

    def set_armor(self, armor):
        self.armor = armor

    ################   THE GEt METHODES     ############
    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_speed(self):
        return self.speed

    def get_lvl(self):
        return self.lvl

    def get_parry(self):
        return self.parry

    def get_dodge(self):
        return self.dodge

    def get_mana(self):
        return self.mana

    def get_room(self):
        return self.room

    ################   THE COMBAT METHODES     ############

    # When player loose the game
    def die(self):   #TODO finish
        self.__init__()

    #displays the buffs currently on the player
    def check_buffs(self):
        print("""Your current boosts are :""")
        for buff in self.buffs:
            print(buff)

    #Clear all the buffs on the player from the previous floor
    def clear_buffs(self):
        for buff in self.buffs:
            if buff == "MAGIC JUICE":
                self.speed -= 200
            if buff == "MONSTER MEAT":
                self.damage -= 5
            if buff == "LIQUID OF THE UNDEAD":
                1
            self.buffs.remove(buff)
            if buff == "FLASK OF THE IMMORTAL":   #you only keep the cheat
                self.buffs.append(buff)

    #method to attack a mob
    def attack(self, enemy):
        dmg = randint(self.damage - self.lvl, self.damage + self.lvl)
        if (randrange(1, 100) + self.crit >= 100):  # if it's a crit
            print("Critical Hit! ")

            enemy.hp = enemy.hp - (dmg * 2)
            print(dmg * 2, " damage done")
        else:
            enemy.hp = enemy.hp - dmg
            print(dmg, " damage done")

    # Called when player is attacked to see if he dodges or parrys the blow
    def dodge_parry(self, mob):
        bad = mob
        self.dodged = False
        dodge = randint(1, 500)
        if (dodge + self.speed) >= 490:
            self.dodged = True
        elif (randint(1, 100) > (100 - self.parry)):
            self.parried = True




    ################   THE CHARACTER METHODES     ############


    def heal_self(self, int):     #not used, (supposed to be used by consumables and magic)
        self.hp = self.hp =+ int
        if self.hp > self.max_hp:
            self.hp = self.max_hp


    #This is called at the end of each floor, the player chooses 2 stats to get an extra boost, also fully heals
    def lvl_up(self):
        self.lvl += 1
        choice1 = int(input(""" You may select 2 stats that will gain an EXTRA permanent boost :
        -HP       (1)              -PARRY   (4) 
        -DAMAGE   (2)              -MANA    (5)
        -SPEED    (3)              -CRIT    (6)
        """
                            ))
        choice2 = int(input(""" You may select 2 stats that will gain an EXTRA permanent boost :
        -HP       (1)              -PARRY   (4) 
        -DAMAGE   (2)              -MANA    (5)
        -SPEED    (3)              -CRIT    (6)
        """))
        if choice2 == choice1:
            print("""You chose the same attribute each time  '__' 
             You don't get any EXXTRA this turn 
             """)
        elif choice1 != choice2:
            if (choice1 == 1) | (choice2 == 1):
                self.max_hp += 10
            if choice1 == 2 | choice2 == 2:
                self.damage += 5
            if choice1 == 3 | choice2 == 3:
                self.speed += 4
            if choice1 == 4 | choice2 == 4:
                self.parry += 2
            if choice1 == 5 | choice2 == 5:
                self.max_mana += 10
            if choice1 == 6 | choice2 == 6:
                self.crit += 2

        self.max_hp += 10
        self.hp = self.max_hp
        self.speed += 4
        self.parry += 1
        self.crit += 2
        self.max_mana += 10
        self.mana = self.max_mana
        self.damage += 5

        ################   THE INVENTORY  METHODES     ############

    #Is called in the Main at the end of a floor, to manage itemss, equiped items etc...
    def manage_items(self):
        self.check_equiped()
        choice = int(input("""YOUR INVENTORY  :
        SHOW INVENTORY     (1)
        MANAGE WEAPONS     (2)
        MANAGE ARMOR       (3)
        MANAGE JEWEL       (4)
           
        """))
        if choice == 1:
            self.display_inventory()
        if choice ==2 :
            if self.equiped!= []:
                if isinstance(self.equiped[0],Weapon):
                    print("Your equiped weapon is ",self.weapon.name,"   +",self.weapon.damage," DAMAGE")
            self.display_weapons()
            weap = input("""
            QUIT   (1)
            EQUIP : Please type the name of the weapon you want to equip 
            
            """)   #Typing is easier, but worse to use   (todo?)
            if weap == "1":
                1
            else:
                for item in self.inventory:
                    if weap == item.name:
                        self.equip(item)
                        break

        if choice ==3 :
            if len(self.equiped) == 2:
                if self.equiped[1] != []:
                    if isinstance(self.equiped[1],Armor):

                        print("Your equiped costume is ",self.armor.name,"   +",self.armor.armor," ARMOR")
                self.display_costumes()
                arm = input("""
                          QUIT   (1)
                          EQUIP : Please type the name of the armor you want to equip 
    
                          """)
                if arm == "1":
                     1
                else:
                    for item in self.inventory:
                        if arm == item.name:
                            self.equip(item)
                            break
            self.equip(item)

        if choice == 4:    #TODO actual effect for the jewel
            if len(self.equiped) == 3:    # so there's no out of bounds errors
                if self.equiped[2] != []:
                    if isinstance(self.equiped[2],Jewel):
                        print("Your equiped jewel is ",self.jewel.name,"   +",self.jewel.bonus)
                self.display_jewels()
                jwl = input("""
                                        QUIT   (1)
                                        EQUIP : Please type the name of the jewel you want to equip 
    
                                        """)
                if jwl == "1":
                    1
                else:
                   for item in self.inventory:
                        if jwl == item.name:
                            self.equip(item)
                            break

        if choice == 5:
            print("HP =",self.hp," MANA =", self.mana)
            self.display_consumables()


    def display_inventory(self):
        if self.inventory == []:
            print("You don't have anything in your inventory :(")
        else:
            print("INVENTORY:    ")
            for item in self.inventory:
                if isinstance(item, Weapon):
                    print("WEAPON : ", item.name, " ", item.description, "  +", item.damage, " DAMAGE")
                if isinstance(item, Armor):
                    print("COSTUME : ", item.name, " ", item.description, "  +", item.armor, " ARMOR")
                if isinstance(item, Jewel):
                    print("JEWEL : ", item.name, " ", item.description, "  +", item.bonus)
                if isinstance(item, Consumable):
                    print("CONSUMABLE : ", item.name, " ", item.description, "  +", item.boost)

    def display_consumables(self):
        for item in self.inventory:
            if isinstance(item, Consumable):
                print(item)
    def display_weapons(self):
        for item in self.inventory:
            if isinstance(item, Weapon):
                print(item)
    def display_costumes(self):
        for item in self.inventory:
            if isinstance(item, Armor):
                print(item)
    def display_jewels(self):
        for item in self.inventory:
            if isinstance(item, Jewel):
                print(item)

    def check_equiped(self):
        if self.equiped == []:
            print("You don't have anything equiped")
        else:
            print("EQUIPPED:    ")
            for item in self.equiped:
                if isinstance(item,Weapon):
                    print("WEAPON : ",item.name," ",item.description,"  +",item.damage," DAMAGE")
                if isinstance(item, Armor):
                    print("COSTUME : ",item.name," ",item.description,"  +",item.armor," ARMOR")
                if isinstance(item,Jewel):
                    print("JEWEL : ",item.name," ",item.description,"  +",item.bonus)
    #To unequip an item
    def unequip(self,item):
        if isinstance(item, Weapon):
            self.damage -= item.damage
        if isinstance(item, Armor):
            self.armor -= item.armor
        if isinstance(item, Jewel):
            print("todo")

    def equip(self,item):
        if isinstance(item, Weapon):
            self.damage += int(item.damage)
            if self.equiped != []:
                self.equiped.pop(0)
            self.equiped[0] = item
            print(item.name, "equiped")
            self.weapon = item
        if isinstance(item, Armor):
            self.armor += int(item.armor)
            if self.equiped != []:
                if len(self.equiped) >= 1:
                    self.equiped.pop(1)
            self.equiped[0] = item
            print (item.name, "equiped")
            self.costume = item
        if isinstance(item, Jewel):
            print("todo")
            if self.equiped != []:
                self.equiped[2] = item
                print(item.name, "equiped")
                self.jewel = item
#########              THE MAGIC 19              ###########

    def get_spell(self, spell):
        self.spells.append(spell)

    def cast_spell(self, mob, spell):     # the player cast a spell on a mob
        if spell.name == "FORCE PUSH":
            if self.mana < spell.cost:
                print("You don't have enough mana to cast this spell")
            else:
                dmg = randint(self.lvl * 5, self.lvl * 10)
                mob.hp = mob.hp - dmg
                self.mana -= spell.cost
                print("You use FORCE PUSH")
                print(dmg," damage done")
        if spell.name == "FIRE BLAST":
            if self.mana < spell.cost:
                print("You don't have enough mana to cast this spell")
            else:
                dmg = randint(self.lvl * 5, self.lvl * 10)
                mob.hp = mob.hp - dmg
                self.mana -= spell.cost
                print("You use FIRE BLAST")
                print(dmg, " damage done")
                print("You burned the enemy !")
                mob.burned = True
                mob.burn(self)
        if spell.name == "MONEY LIFE ":
            if self.mana < spell.cost:
                print("You don't have enough mana to cast this spell")
            else:
                mob.money *= 2
                print("You use MONEY LIFE")
                self.mana -= spell.cost
        if spell.name == "MAGIC POISON":
            if self.mana < spell.cost:
                print("You don't have enough mana to cast this spell")
            else:
                mob.hp /= 2
                mob.damage *= 2
                self.mana -= spell.cost
                print("You use MAGIC POISON")
        if spell.name == "MAGIC ROULETTE":
            if self.mana < spell.cost:
                print("You don't have enough mana to cast this spell")
            else:
                rand = randint(1,6)
                if rand == 1:
                    print("Your spell misfired and ended up killing you, that's too bad ")
                    self.die()
                if rand == 2 or rand == 3:
                    mob.hp = 0
                    print("You hit the target with a deadly spell! This is a KO! ")
                if rand == 4 or rand ==5:
                    mob.hp -= self.lvl^2
                    print("ohh, your spell barely missed, unlucky !")
                if rand == 6 :
                    mob.hp += self.lvl^2
                    print("You just healed the enemy with your spell, careful! ")
                self.mana -= spell.cost
    def display_spells(self):
        for spell in self.spells:
            print(spell)

########### The merchant class, sells and buys different item   ##########
class Merchant:    #TODO implement
    def __init__(self, name, description, gold, items):
        self.name = name
        self.description = description
        self.gold = gold
        self.items = items
        self.inventory = []

    #Called to trade with a player
    def trade(self,player, int):
        print(self.inventory)
        print(self.inventory[int - 1].price)
        if player.gold < self.inventory[int - 1].price:
            print("You can't afford this !! ")
        else:
            player.inventory.append(self.inventory[int - 1])    #-1 cause the input is 1-9
            player.gold -= self.inventory[int-1].price
            self.gold += self.inventory[int-1].price
            self.inventory.pop(int-1)
            print("item traded !")

### This is to create the merchants inventory
## Better way to create the inventory, no need to use the .txt file
    def make_inventory(self):     ##### TODO: only adds one item, doesn't work
        split = self.items.split(",")
        for k in range (len(split)):
            for item in inv.items :
                if split[k] == item.name :
                    self.inventory.append(item)
            k += 1







##################    THE MOTHER CLASS OF THE ENEMIES IN THE GAME    ################
class Enemy():
    def __init__(self, name, description, damage, hp, lvl, speed, drop, money):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.lvl = lvl
        self.speed = speed
        self.description = description
        self.drop = drop
        self.money = money
        self.burned = False


    #The enemy attacks the player, called during a fight, damage taken is % to the player.parry and player.dodge
    def attack(self, player):
        player.dodge_parry(self)  #  is called to check if the player dodged the attack
        if not player.dodged:
            if not player.parried:
                player.hp = player.hp - (self.damage- player.armor)
                print("You took ",(self.damage- player.armor), "damage from ", self.name)
            else:
                player.hp = player.hp - ((self.damage- player.armor) - player.parry)
                print("Nice parry!")
                print("You took a reduced", (self.damage- player.armor) - player.parry, "damage from ", self.name)
        elif player.dodged:
            print("You dodged the attack !")

    #this method is called when a monster dies, to check the drops
    def to_drop(self, player):      #TODO method so i don't have to open .txt every time
        drop_done = False
        if self.drop == "null":
            drop_done = True
        filepath = 'items.txt'
        file = open(filepath, "r")
        while not drop_done:  # drop is a String from the .txt
            if "/" in self.drop:   # checks if the mob can drop two items ( separated by the "/" in the .txt )
                drops = self.drop.split("/")   #splits the two items
                drop1 = drops[0].split(",")     #splits again each item
                drop2 = drops[1].split(",")
                rand1 = randint(1, 100)
                rand2 = randint(1, 100)
                for line in file:    # checks through each item for the right name ////  time lost because of the constructor of the Items classes
                    split = line.split(";")
                    if split[0] == "Weapon":
                        if rand1 >= int(drop1[1]) and drop1[0] == split[1]:
                            player.inventory.append(Weapon(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                        elif rand2 >= int(drop2[1]) and drop2[0] == split[1]:
                            player.inventory.append(Weapon(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                    if split[0] == "Armor":
                        if rand1 >= int(drop1[1]) and drop1[0] == split[1]:
                            player.inventory.append(Armor(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                        elif rand2 >= int(drop2[1]) and drop2[0] == split[1]:
                            player.inventory.append(Armor(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                    if split[0] == "Jewel":
                        if rand1 >= int(drop1[1]) and drop1[0] == split[1]:
                            player.inventory.append(Jewel(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                        elif rand2 >= int(drop2[1]) and drop2[0] == split[1]:
                            player.inventory.append(Jewel(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                    if split[0] == "Consumable":
                        if rand1 >= int(drop1[1]) and drop1[0] == split[1]:
                            player.inventory.append(Consumable(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                        elif rand2 >= int(drop2[1]) and drop2[0] == split[1]:
                            player.inventory.append(Consumable(split[1], split[2], split[3], split[4]))
                            print("The monster dropped something : ", split[1])
                drop_done = True
            else:   #################### If the monster can drop only one item (most cases)   //// Same way and same problems
                rand = randint(1, 100)
                drops = self.drop.split(",")
                for line in file:
                    split = line.split(";")
                    if split[0] == "Weapon":
                         if rand >= int(drops[1]) and drops[0] == split[1]:
                             player.inventory.append(Weapon(split[1], split[2], split[3], split[4]))
                             print("The monster dropped something : ", split[1])
                    if split[0] == "Armor":
                         if rand >= int(drops[1]) and drops[0] == split[1]:
                             player.inventory.append(Armor(split[1], split[2], split[3], split[4]))
                             print("The monster dropped something : ", split[1])
                    if split[0] == "Jewel":
                         if rand >= int(drops[1]) and drops[0] == split[1]:
                             player.inventory.append(Jewel(split[1], split[2], split[3], split[4]))
                             print("The monster dropped something : ", split[1])
                    if split[0] == "Consumable":
                         if rand >= int(drops[1]) and drops[0] == split[1]:
                             player.inventory.append(Consumable(split[1], split[2], split[3], split[4]))
                             print("The monster dropped something : ", split[1])
                drop_done = True

    #applied if the player use the fire blast spell, is called during a fight at the start of the turn
    def burn(self, player):
        rand = randint(player.lvl, player.lvl + 4)
        self.hp -= rand


#Subclasses for enemy
class Mob(Enemy):
    def __init__(self, name, description, damage, hp, lvl, speed, drop, money):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.lvl = lvl
        self.speed = speed
        self.description = description
        self.drop = drop
        self.money = money
        self.burned = False

#TODO Boos class // power is meant to be a 2nd attack unique to each boss, used "randomly"
class Boss(Enemy):
    def __init__(self, name, description, damage, hp, lvl, speed, power, drop, money):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.lvl = lvl
        self.speed = speed
        self.power = power
        self.description = description
        self.drop = drop
        self.money = money
        self.burned = False
