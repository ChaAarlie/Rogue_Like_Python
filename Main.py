import time

from Magic import Spell
from Map import *
from Menu import Menu
from characters import Player
from inventory import *


def gen_spells():  # generates the spells from txt file and put them in list, to be used by player
    filepath = 'spells.txt'
    file = open(filepath, "r")
    for line in file:
        split = line.split(";")
        spellss.append(Spell(split[0], split[1], split[2], int(split[3])))


player = Player()
map = Map()  # the map for the game
mobkilled = 0
menu = Menu()  # the menu
game_on = False
spellss = []  # contains all the spells
gen_spells()
inv = Inventory()
inv.god_inventory()
# player.inventory = inv           #cheat, gives player all items in the game
# player.equiped[2] = inv.items[len(inv.items -1 )]    #  gives player the cheat item

for i in range(len(spellss)):  # for now, the player starts with all the spellss
    player.spells.append(spellss[i])


def start_game():  # ?
    player.room = 1


##ACTUAL GAME##
class Main():  # TODO: put in methods
    start_game()
    game_on = True
    while game_on:
        map.gen_map(player)
        map.gen_mobs()
        map.gen_merchants()
        map.gen_rooms(player)
        player.floor += 1
        player.clear_buffs()  # removes the buffs from consumable frm previous floor
        print("You enter the ", player.floor, " floor, good luck!")
        for j in range(len(map.map)):  # go through all the map
            player.winner = False
            if map.map[j].y_enemy:  # if there is an enemy in the room
                if map.map[j].y_boss:
                    mob = map.map[j].boss
                else:
                    mob = map.map[j].mob  # Map class contains map list(Room)
                print("Un ennemie apparait! ")
                while not player.winner:  # until the fight is over
                    choice = menu.combat(player, mob)  # the combat menu
                    if mob.burned:         #burn damage at the start of each turn
                        mob.burn(player)
                    if choice == 1:  # player attacks the mob
                        if mob.speed > player.speed:
                            mob.attack(player)
                            if player.hp < 0:
                                player.die()
                                game_on = False
                                break
                            else:
                                player.attack(mob)
                        elif mob.speed < player.speed:  # check each time if no one died
                            player.attack(mob)
                            if mob.hp > 0:
                                mob.attack(player)
                                if player.hp < 0:
                                    player.die()
                                    game_on = False
                                    player.winner = False
                                    break
                        if mob.hp <= 0:
                            mobkilled += 1  # kill count (for stats and achievment (TODO))
                            mob.to_drop(player)  # check if mob drops an item
                            print("You win this battle, you may carry on...")
                            player.winner = True

                            time.sleep(1)

                    if choice == 2:
                        print('You have this spells available :')
                        player.display_spells()
                        decision = input(""" Type the name of the spell you want to use: """)
                        for spell in spellss:
                            if spell.name == decision:
                                player.cast_spell(mob, spell)
                                if mob.hp <= 0:
                                    mobkilled += 1  # kill count (for stats and achievment (TODO))
                                    mob.to_drop(player)  # check if mob drops an item
                                    print("You win this battle, you may carry on...")
                                    player.winner = True
                                    time.sleep(1)

                    if choice == 3:  # Player use Consumable
                        print(player.display_consumables())
                        ahaha = int(input("""Do you want to use a consumable ?
                                YES  (1)        NO   (2)
                        """))
                        if ahaha == 1:
                            decision = input(
                                """ Type the name of the consumable you want to use: """)  # TODO better way (menu?)
                            if decision == "WATER":
                                player.hp += (10 / 100) * player.max_hp  # heals 10% hp
                                if player.hp > player.max_hp:
                                    player.hp = player.max_hp
                                for item in player.inventory:
                                    if item.name == "WATER":
                                        player.inventory.remove(item)
                                        break  # so it dosn't remove all of the selected item

                            if decision == "MAGIC JUICE":
                                player.speed += 200  # temporary max speed removed at the start of next floor in check_buffs()
                                player.hp += (20 / 100) * player.max_hp  # heals 20%
                                if player.hp > player.max_hp:
                                    player.hp = player.max_hp
                                player.buffs.append(decision)  # a list with all the buffs currently on the player
                                for item in player.inventory:
                                    if item.name == "MAGIC JUICE":
                                        player.inventory.remove(item)
                                        break
                            if decision == "RABID DOG MEAT":
                                player.hp += 30
                                if player.hp > player.max_hp:
                                    player.hp = player.max_hp
                                for item in player.inventory:
                                    if item.name == "RABID DOG MEAT":
                                        player.inventory.remove(item)
                                        break

                            if decision == "MONSTER MEAT":  # gives temp bonus.for the current floor
                                player.hp += 10
                                if player.hp > player.max_hp:
                                    player.hp = player.max_hp
                                player.damage += 5 * player.lvl
                                player.buffs.append(decision)
                                for item in player.inventory:
                                    if item.name == "MONSTER MEAT":
                                        player.inventory.remove(item)
                                        break
                            if decision == "LIQUID OF THE UNDEAD":
                                player.buffs.append(
                                    decision)  # gets you back to life when you die (TODO in player.die() check if player.buffs contains )
                                for item in player.inventory:
                                    if item.name == "LIQUID OF THE UNDEAD":
                                        player.inventory.remove(item)
                                        break
                            if decision == "RED POTION":
                                player.hp += player.hp * 2
                                if player.hp > player.max_hp:
                                    player.hp = player.max_hp
                                    for item in player.inventory:
                                        if item.name == "RED POTION":
                                            player.inventory.remove(item)
                                            break
                            if decision == "FLASK OF THE IMMORTAL":  # cheat item
                                player.hp += 1000
                                player.damage += 1000
                                player.speed += 1000
                                player.buffs.append(decision)
                                for item in player.inventory:
                                    if item.name == "FLASK OF THE IMMORTAL":
                                        player.inventory.remove(item)
                                        break

            elif map.map[j].y_merchant:  # if there's a merchant in this room
                alal = menu.trade(player, map.map[j].merchant)
                player.room += 1
                if alal == 1:
                    a = 1
                    trading = True
                    map.map[j].merchant.make_inventory()
                    print("""Here's what I have to sell, traveler:""")
                    while trading:
                        if len(map.map[j].merchant.inventory) == 0:    #
                            break
                        for items in map.map[j].merchant.inventory:
                            print(items.name, "  ", items.price, "(", a, ")")
                        lala = input("What item do you want to buy ?   (9) exit  ")
                        if lala == 9:
                            trading = False
                        else:
                            map.map[j].merchant.trade(player, int(lala))


            elif map.map[j].y_treasure:  # if there's a treasure (Rare Item)
                print("!!!!!!!salle au trésor!!!!!!")
            else:
                bla = int(input("You enter an empty room, take your time and press (1) to get out"))
        if player.hp <= 0:  # because the method player.die doesn't work yet'
            print("You lost, too bad so sad")
            game_on = False
            break
        choice = 0
        print("You finished this floor! Congratulation!")
        player.lvl_up()
        if player.floor % 5 == 0:  # If this was a floor with a Boss (multiple of 5), stage += 1
            player.stage += 1
        while choice != 3:
            choice = int(input("""
            Prepare to enter the next floor:
            Change your items (1)
            Change your magic (2)
            Go to the next floor (3)
            """))
            if choice == 1:
                player.manage_items()
            if choice == 2:
                print("This is yet to be done ")  # not be done because player has all spells from the start (for now)
            if choice == 3:
                print("Entering next floor")
