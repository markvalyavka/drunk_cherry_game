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

    def set_description(self, description):
        self.description = description

    def set_items(self, items):
        self.items = items

    def set_guardian(self, character):
        self.guardian = character

    def get_details(self):
        return "*Details*"

    def link_street(self, other_street, direction):
        self.travel_possibilities[direction] = other_street


class Item:

    def __init__(self, item_name, item_type):

        self.item_name = item_name
        self.item_type = item_type


    def set_description(self, description):
        self.description = description

    def describe(self):
        return "You see a [{}]  -  {}".format(self.item_name,
                                              self.description)

