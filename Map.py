from random import *
from characters import *


############    TO GENERATE THE MAP, ENEMIES AND MERCHANT OF THE MAP     ############

class Map():  ## This is the map for an entire lvl, the map is linear with a randomly generated size which depends on the player lvl

    def __init__(self, map=None, enemies=None, mobs=None, merchants=None, boss=None):    ###These Arrays contain all the infos of the different parts of the game
        if map is None:
            map = []
        if enemies is None:
            enemies = []
        if mobs is None:
            mobs = []
        if merchants is None:
            merchants = []
        if boss is None:
            boss = []
        self.map = map
        self.enemies = enemies
        self.mobs = mobs
        self.merchants = merchants
        self.boss = boss

    def get_size(self):   #useless
        return len(map)

    def gen_map(self, player):  # Generates the map for the level (it's size)
        self.map = []  # clear the previous map
        rand = randrange((player.lvl + 5 + ((player.lvl + 5) % 2)) / 2,
                         player.lvl + 5)  # modulo so it's always an Integer
        self.enemies = []
        for i in range(rand):
            if (randint(1, 100) > 25):  # about 3/4 for an enemy to spawn in a map
                self.enemies.append(1)
            else:
                self.enemies.append(0)

    #This method generates all the room for current floor
    #Also creates the Mob if it is a room with an enemy
    #Same for merchant and Treasures (TODO)
    def gen_rooms(self, player):
        for j in range(len(self.enemies)):   #for each room
            if self.enemies[j] == 1:
                room = Room()
                room.y_enemy = True

                cent = randint(1, 100)   ##This is to determine which Mob is gonna be spawned
                if cent <= 50:
                    rand = 0 + (player.stage * 3)  #common
                if 51 < cent <= 90:
                    rand = 1 + (player.stage * 3)   #uncommon
                if 91 < cent <= 100:
                    rand = 2 + (player.stage * 3)    #rare mob
                ###The following is the attempt to balance the game
                dmg = randint(self.mobs[rand].damage - 1 , self.mobs[rand].damage + 10 * player.floor)
                hp = randint(self.mobs[rand].hp - 2 * player.lvl, self.mobs[rand].hp + 10 * player.floor)
                speed = randint(self.mobs[rand].speed - 2 * player.speed, self.mobs[rand].speed + 10 * player.floor)
                lvl = self.mobs[rand].lvl + player.lvl - 1
                name = self.mobs[rand].name
                description = self.mobs[rand].description
                drop = self.mobs[rand].drop
                money = self.mobs[rand].money
                if rand == 2:     #Rare mob is extra strong
                    hp = randint(self.mobs[rand].hp * player.lvl, self.mobs[rand].hp + 10 * player.lvl)

                room.mob = Mob(name, description, dmg, hp, lvl, speed, drop, money)
                self.map.append(room)
                if j == len(self.enemies):   #the last room
                    if player.lvl % 5 == 0:     #  if it's a floor with a boss (5,10,15,20,..)
                        boss_room = Room()
                        boss_room.y_enemy = False
                        boss_room.y_boss = True
                        room.boss= self.boss[player.stage]
                        self.map.remove(room)    #remove the mob to put the boss
                        self.map.append(boss_room)

            elif (self.enemies[j] == 0):    ##if there's no enemy in the room
                if (randint(1, 5) != 5):   ## 4/5 chance to spawn a Merchant in an empty room
                    room = Room()
                    room.merchant = self.merchants[player.stage]   #1 type of merchant per stage
                    room.y_merchant = True
                    self.map.append(room)

                else:    ##TODO make treasure room
                    room = Room()
                    self.map.append(room)

            elif (self.enemies[j] == 2):
                room = Room()
                room.y_boss = True
                self.map.append(room)

    #get all the mobs of the gam from the .txt file
    def gen_mobs(self):
        self.mobs = []
        filepath = 'mobs.txt'
        file = open(filepath, "r")
        for line in file:
            split = line.split(";")
            self.mobs.append(
                Mob(split[0], split[1], int(split[2]), int(split[3]), int(split[4]), int(split[5]), split[6],
                    int(split[7])))

    def gen_boss(self):
        self.mobs = []
        filepath = 'boss.txt'
        file = open(filepath, "r")
        for line in file:
            split = line.split(";")
            self.boss.append(
                Boss(split[0], split[1], int(split[2]), int(split[3]), int(split[4]), int(split[5]), split[6],
                    int(split[7],split[8])))

    def gen_merchants(self):
        self.merchants = []
        filepath = 'merchants.txt'
        file = open(filepath, "r")
        for line in file:
            split = line.split(";")
            self.merchants.append(Merchant(split[0], split[1], int(split[2]), split[3]))


# class room, an instance of this class is created for each map[i]
## it contains either a mob, the boss, the merchant or a treasure!!
class Room():

    def __init__(self, mob=None, merchant=None, boss=None):
        if mob is None:
            mob = Mob
        self.mob = mob
        if merchant is None:
            merchant = Merchant
        self.merchant = merchant
        if boss is None:
            boss = Boss
        self.merchant = merchant
        self.y_enemy = False
        self.y_merchant = False
        self.y_treasure = False
        self.y_boss = False
