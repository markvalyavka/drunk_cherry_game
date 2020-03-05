"""
All classes objects in the game.
"""


class Street:

    def __init__(self, street_name):

        self.street_name = street_name
        self.description = None
        self.items = None
        self.guardian = None
        self.travel_possibilities = {}

    def __str__(self):
        return self.street_name

    def set_description(self, description):
        self.description = description

    def set_items(self, items):
        self.items = items

    def set_guardian(self, character):
        self.guardian = character

    def get_details(self):
        print("{}\n-------------\n{}\n".format(self.street_name,
                                               self.description))

        if (self.items) and (self.items is not None):
            for item in self.items:
                print(item.describe())
        print("\n", end="")
        if self.travel_possibilities:
            for direction in self.travel_possibilities:
                street = self.travel_possibilities[direction]
                print(f'{street.street_name} is to the {direction}')
        print("-------------\n")

    def print_items(self):
        print("\n", end="")
        if (self.items) and (self.items is not None):
            for item in self.items:
                print(item.describe())
        print("\n", end="")

    def get_actions(self):

        print("\n", end="")
        actions_available_print = ""
        if self.items:
            actions_available_print += "\t| take |"

        if self.travel_possibilities:
            actions_available_print += "\t| move |"

        actions_available_print += "\t| backpack |"

        print(actions_available_print)
        print("\n", end="")


    def link_street(self, other_street, direction):
        self.travel_possibilities[direction] = other_street


class Item:

    def __init__(self, item_name, item_type):

        self.item_name = item_name
        self.item_type = item_type

    def __str__(self):
        return self.item_name

    def __repr__(self):
        return self.item_name

    def set_description(self, description):
        self.description = description

    def describe(self):
        return "You see a [{}]  -  {}".format(self.item_name,
                                              self.description)

