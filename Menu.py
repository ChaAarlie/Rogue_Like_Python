import time


######## THIS WAS SUPPOSED TO CONTAINS ALL THE MENUS OF THE GAME  #######
#Menu only usefull for the combat, TODO all the others (Magic, consumables, lvl up , etc..)
class Menu() :
    def intro(self):
        print(""" Preparez vous à rentrer dans la tour! 

                      Vous ouvrez la porte:

                      1er étage! """)

    def combat(self, player, enemy):
        #choice = 0
        time.sleep(1)
        print("  "
              ""
              "  VERSUS  :          lvl", player.lvl," ", enemy.name, "   HP :",enemy.hp,"""
          """,enemy.description,"""
        
        
             YOUR HP: """, player.hp,"/",player.max_hp,"    YOUR MANA: ", player.mana, "/", player.max_mana,"""
                             VOS ACTIONS DISPONIBLES:
            ATTACK   (1)           !MAGIC!     (2)         CONSUMABLE      (3)
        """)
        #while choice != 1 & choice !=2 & choice != 3 :
        choice = int(input(" "))
        return choice

    def trade(self, player, merchant):
        # choice = 0
        time.sleep(1)
        print("""   You encountered the merchant!!
        """,merchant.name,"""          """,merchant.description,"""
        """,merchant.gold," gold","""
                                            
        ITEMS:   """,merchant.items,"""
                             VOS ACTIONS DISPONIBLES:
                   TRADE   (1)                      !LEAVE!     (2)      
        """)
        # while choice != 1 & choice !=2 & choice != 3 :
        choice = int(input(" "))
        return choice