"""
Module to represent entities in the game.
"""


class Player:

    def __init__(self, current_street=None):

        self.lives = 3
        self.backpack = []
        self.weapons = []
        self.friends = []
        self.current_street = current_street

    def add_to_backpack(self, item):

        if item.type == "weapon":
            self.weapons.append(item)
        else:
            self.backpack.append(item)

    def set_current_street(self, current_street):

        self.current_street = current_street


    def move(self, direction):

        if direction in self.current_street.travel_possibilities:

            if self.current_street.travel_possibilities[direction].guardian is not None:
                self.current_street.travel_possibilities[direction].guardian.interaction()

            self.current_street = self.current_street.travel_possibilities[direction]
            self.current_street.get_details()

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
        print(self.talk_phrase)

    def set_interaction(self, interaction_name, interaction_func):

        self.interaction_options[interaction_name] = interaction_func

    def describe(self):

        if self.character_type == "guardian":
            print("Oii, you can't pass through a nasty {},\n"
                  "who guards the street.\nYou see {}  -  {}\n".format(self.status,
                                                                       self.character_name,
                                                                       self.description))

        elif self.character_type == "ordinary":
            print("Someone is moving towards you. Is it a ..?\n"
                  "You see {}, named {}".format(self.description,
                                                self.character_name))


    def show_interaction_options(self):

        if self.interaction_options:
            for interaction in self.interaction_options:
                print("\n\t| {} |   ".format(interaction))
        else:
            print("You can't interact with this person.")


    def interaction(self):
        self.describe()
        option = "leave"

        while option != "leave":
            self.show_interaction_options()
            option = input(">  ")
            if option in self.interaction_options:
                self.interaction_options[option]()
            else:
                print("You can't do that!")


class Guardian(Character):

    def __init__(self, character_name):

        super().__init__(character_name)
        self.character_type = "guardian"

