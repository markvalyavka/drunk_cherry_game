"""
Module to represent entities in the game.
"""


class Player:

    def __init__(self, current_street=None):

        self.lives = 3
        self.backpack = []
        self.friends = []
        self.current_street = current_street

    def __str__(self):
        return "Player on {}".format(self.current_street)

    def add_to_backpack(self, item):

        self.backpack.append(item)

    def see_backpack(self):
        print("")
        print("Backpack: {}".format(self.backpack))
        print("")

    def item_choice(self):
        self.see_backpack()

        if self.backpack:
            while True:
                print("What item to you want to choose?")
                item = input("-->  ")
                for item_b in self.backpack:
                    if item_b.item_name == item:
                        return item_b
                else:
                    print("You have no {} in your backpack!".format(item))
        else:
            print("You have no items!")

    def set_current_street(self, current_street):

        self.current_street = current_street

    def fight(self, character, weapon):

        if weapon in self.backpack:
            if weapon.item_type == "weapon":
                if weapon.item_name == character.weakness:
                    self.current_street.guardian = None
                    self.backpack.remove(weapon)
                    print("Flawless win! You can now go. Poor {}".format(character.character_name))
                    return True
                else:
                    self.lives -= 1
                    print("Not today boy! And don't even come back here!")
                    return False
            else:
                print("Ehm, seems like you can't fight with that")
                return False
        else:
            print("You don't have {} in your backpack".format(weapon.item_name))
            return False

    def become_friends(self, character, item):

        if item in self.backpack:
            if item.item_type == "ordinary":
                if item.item_name == character.loved_item:
                    self.current_street.guardian = None
                    self.backpack.remove(item)
                    print("Wow, thanks for {}.\nWell, i guess you can go.\n"
                          "We're friends now =)".format(item.item_name))
                    self.friends.append(character)
                    return True
                elif item.item_name == character.hated_item:
                    print("[*Hits you*] . You know what? Go to hell and neve comeback!!".format(item.item.item_name))
                    self.lives -= 1
                    return False
                else:
                    print("Why are you giving me {}. Think this is funny?".format(item.item.item_name))
                    return False
            else:
                print("I think its a bad idea to become friends with someone using that")
                return False
        else:
            print("You don't have {} in your backpack".format(item.item_name))
            return False

    def take(self, item):

        for item_p in self.current_street.items:
            if item_p.item_name == item:
                self.current_street.items.remove(item_p)
                self.backpack.append(item_p)
                break
        else:
            print("Such item doesn't exist!")

    def move(self, direction):

        if direction in self.current_street.travel_possibilities:

            street_guardian = self.current_street.travel_possibilities[direction].guardian

            if street_guardian is not None:
                street_guardian.describe()
                while True:
                    player_choice = street_guardian.interaction()
                    if player_choice == "fight":
                        item = self.item_choice()
                        if self.fight(street_guardian, item):
                            self.current_street = self.current_street.travel_possibilities[direction]
                            self.current_street.guardian = None
                            break

                    elif player_choice == "become friends":
                        item = self.item_choice()
                        if self.become_friends(street_guardian, item):
                            self.current_street = self.current_street.travel_possibilities[direction]
                            self.current_street.guardian = None
                            break

                    elif player_choice == "talk":
                        street_guardian.talk()
                    elif player_choice == "leave":
                        break

            else:
                self.current_street = self.current_street.travel_possibilities[direction]

        else:
            print("Ouuf, seems like you're lost.\nYou can't go {}".format(direction))







class Character:

    status = "character"

    def __init__(self, character_name, character_type="ordinary"):

        self.character_name = character_name
        self.character_type = character_type
        self.description = None
        self.weakness = None
        self.loved_item = None
        self.hated_item = None
        self.talk_phrase = None
        self.fight_phrase = None
        self.friend_phrase = None
        self.interaction_options = {}

    def __str__(self):
        return "\n{} called {}  -  {}".format(self.status,
                                            self.character_name,
                                            self.description)

    def __repr__(self):
        return "{} called {}".format(self.status,
                                     self.character_name)

    def set_description(self, description):
        self.description = description

    def set_weakness(self, weakness):
        self.weakness = weakness

    def set_loved_item(self, item):
        self.loved_item = item

    def set_hated_item(self, item):
        self.hated_item = item

    def set_conversation_phrases(self, talk_phrase=None,
                                       fight_phrase=None,
                                       friend_phrase=None):

        self.talk_phrase = talk_phrase
        self.fight_phrase = fight_phrase
        self.friend_phrase = friend_phrase

    def talk(self):
        print("[{} says]: {}".format(self.character_name, self.talk_phrase))
        return False

    def fight(self):
        print(self.fight_phrase)

    def become_friend(self):
        print(self.friend_phrase)

    def set_interaction(self, interaction_name):

        if interaction_name == "fight":
            interaction_func = self.fight
        elif interaction_name == "talk":
            interaction_func = self.talk
        elif interaction_name == "become friends":
            interaction_func = self.become_friend
        self.interaction_options[interaction_name] = interaction_func

    def describe(self):

        if self.character_type == "guardian":
            print("Oii, you can't pass through a nasty {},"
                  "who guards the street.\nYou see {}  -  {}\n".format(self.status,
                                                                       self.character_name,
                                                                       self.description))

        elif self.character_type == "ordinary":
            print("Someone is moving towards you. Is it a ..?\n"
                  "You see {}, named {}".format(self.description,
                                                self.character_name))


    def show_interaction_options(self):

        if self.interaction_options:
            print("\n", end="")
            for interaction in self.interaction_options:
                print("\t| {} |   ".format(interaction), end="")
            print("\t| leave |   ", end="")
            print("\n")
        else:
            print("You can't interact with this person.")


    def interaction(self):
        option = None

        while option != "leave":
            self.show_interaction_options()
            option = input(">  ")
            print("\n", end="")
            if option == "leave": return option
            if option in self.interaction_options:
                return option
            else:
                print("You can't do that!")



class Guardian(Character):

    status = "guardian"

    def __init__(self, character_name):

        super().__init__(character_name)
        self.character_type = "guardian"


