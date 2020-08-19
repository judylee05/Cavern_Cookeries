class Player:
    """Represents the Player character"""

    def __init__(self, cavern_level, row, column):
        """Initializes the Player character"""
        self._name = "You"
        self._inventory = []
        self._location = [cavern_level, row, column]
        self._max_hp = 50
        self._hp = 50
        self._dice = {
            "attack": "2d6",
            "defense": "2d6"
        }

    def get_name(self):
        """Returns the Player's name"""
        return self._name

    def get_hp(self):
        """Returns the Player's HP"""
        return self._hp

    def get_max_hp(self):
        """Returns the Player's max HP"""
        return self._max_hp

    def set_hp(self, new_hp):
        """Sets/updates the Player's HP to be the new HP value"""
        self._hp = new_hp

    def get_dice(self):
        """Returns the Player's dice for attack and defense"""
        return self._dice

    def get_location(self):
        """Returns the Player's location"""
        return self._location

    def set_location(self, new_level, new_row, new_col):
        """Sets/updates the Player's location"""
        self._location = [new_level, new_row, new_col]

    def get_inventory(self):
        """Returns the Player's inventory"""
        return self._inventory

    def add_inventory(self, item):
        """Adds item (string) to the Player's inventory and sorts inventory alphabetically"""
        self._inventory.append(item)
        self._inventory.sort()