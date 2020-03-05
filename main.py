"""
Main game module.
"""


from game.entities import Player, Character, Guardian
from game.objects import Street, Item

import time


#Create entities


guardian1 = Guardian("Mr.Drunkhead")
guardian1.set_description("A 20-year-old student who left a university because of "
                          "alkohol addiction. Hates literature, and works as a guardian")
guardian1.set_weakness("sharp bottle")
guardian1.set_loved_item("whiskey")
guardian1.set_hated_item("book")
guardian1.set_conversation_phrases("What are you lookin' at?!", "War phrase", "Ma friend")
guardian1.set_interaction("fight")
guardian1.set_interaction("talk")
guardian1.set_interaction("become friends")

#Create items
item1 = Item("book", "friendly")
item1.set_description("'Franko's Poems' - quite an old book that *for some reason* lied on the Franko Street")

item2 = Item("sharp bottle", "weapon")
item2.set_description("'Rozochka' - weapon well-know to people born in 1990s")

item3 = Item("whiskey", "friendly")
item3.set_description("'Proper Twelve' - a bottle of the notorious Irish whiskey by Conor Mcgregor")

#Generate playing field
street1 = Street("Ivana Franka Street")
street1.set_description("A nice old street with a park nearby, leading towards the city centre.")
street1.set_items([item1, item2, item3])




street2 = Street("Volos'ka Street")
street2.set_description("A street with an old history. It even smells like 400 years ago.")
street2.set_guardian(guardian1)

street3 = Street("Zelena Street")
street3.set_description("This streets name doesn't reflect a real situation.")

street4 = Street("Vinnichenka Street")
street4.set_description("A street full of landmarks - two shops and a bus stop.")

street5 = Street("Arsenal'na Street")
street5.set_description("Drunk cherry drink seems so close. You can smell it in the air on this street")

#Link streets
street1.link_street(street2, "north")


player = Player()
player.set_current_street(street1)


if __name__ == "__main__":

    while player.lives > 0:
        player.current_street.get_details()
        player.current_street.get_actions()
        action = input("-->  ")
        if action == "take":

            take_action = "yes"
            while (take_action not in ["no", "nope", "No"]) and (player.current_street.items):

                print("What do you want to take?")
                item_taken = input("-->  ")
                player.take(item_taken)

                player.current_street.print_items()
                if player.current_street.items:
                    print("Want to take something more? [yes/no]")
                    take_action = input("-->  ")

        elif action == "move":
            print("Where do you want to go?")
            move_action = input("-->  ")
            player.move(move_action)
            print("")

        elif action == "backpack":
            player.see_backpack()
            time.sleep(3)


        # print(player.backpack)











if __name__ == "__main__":

    pass