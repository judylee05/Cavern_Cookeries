class Monster:
    """Parent class for Monster objects in the Cavern"""

    def __init__(self, subtype, cavern_level, row, col):
        """Initializes Monster object"""

        # subtype will be either "a" or "b" - each drops different item
        self._subtype = subtype
        self._location = [cavern_level, row, col]

        # will specify type and drop once Parent class is inherited
        self._type = None
        self._title_a = None
        self._title_b = None
        self._drop_a = None
        self._drop_b = None
        self._hp = None
        self._max_hp = None
        self._dice = {
            "attack": "1d6",
            "defense": "1d6"
        }

    def __repr__(self):
        """To help with printing/testing by printing a label for each Monster on the map"""
        if self._subtype == "a":
            # return "a" + self._type[0]
            return self._type[0]
        else:
            # return "b" + self._type[0]
            return self._type[0]

    def get_name(self):
        """Returns the full title of the Monster (ex. "Shy Slime")"""
        if self._subtype == "a":
            name = self._title_a + " " + self._type
        else:
            name = self._title_b + " " + self._type
        return name

    def get_type(self):
        """Returns the Monster's type"""
        return self._type

    def get_location(self):
        """Returns the Monster's location"""
        return self._location

    def set_location(self, new_level, new_row, new_col):
        """Sets/updates the location of the Monster"""
        self._location = [new_level, new_row, new_col]

    def get_drop(self):
        """Returns the Monster's dropped item"""
        if self._subtype == "a":
            return self._drop_a
        else:
            return self._drop_b

    def get_hp(self):
        """Returns the Monster's HP"""
        return self._hp

    def get_max_hp(self):
        """Returns the Monster's max HP"""
        return self._max_hp

    def get_dice(self):
        """Returns the Monster's dice for attack and defense"""
        return self._dice


class Slime(Monster):
    """Slime Monster Class"""
    def __init__(self, subtype, cavern_level, row, col):
        super().__init__(subtype, cavern_level, row, col)

        self._type = "Slime"
        self._title_a = "Shy"
        self._title_b = "Stinky"
        self._drop_a = "Chewy Gelatin"
        self._drop_b = "Slippery Ooze"
        self._hp = 10
        self._max_hp = 10


class Treant(Monster):
    """Treant Monster Class"""
    def __init__(self, subtype, cavern_level, row, col):
        super().__init__(subtype, cavern_level, row, col)

        self._type = "Treant"
        self._title_a = "Talkative"
        self._title_b = "Talentless"
        self._drop_a = "Funky Fruit"
        self._drop_b = "Tree Syrup"
        self._hp = 16
        self._max_hp = 16
        self._dice = {
            "attack": "1d6",
            "defense": "1d6"
        }

class Chimera(Monster):
    """Chimera Monster Class"""
    def __init__(self, subtype, cavern_level, row, col):
        super().__init__(subtype, cavern_level, row, col)

        self._type = "Chimera"
        self._title_a = "Charming"
        self._title_b = "Clumsy"
        self._drop_a = "Chimera Egg"
        self._drop_b = "Mystery Meat"
        self._hp = 20
        self._max_hp = 20
        self._dice = {
            "attack": "2d6",
            "defense": "2d6"
        }

class Octopus(Monster):
    """Octopus Monster Class"""
    def __init__(self, subtype, cavern_level, row, col):
        super().__init__(subtype, cavern_level, row, col)

        self._type = "Octopus"
        self._title_a = "Ostentatious"
        self._title_b = "Outstanding"
        self._drop_a = "Octopus Ink"
        self._drop_b = "Giant Tentacle"
        self._hp = 22
        self._max_hp = 22
        self._dice = {
            "attack": "2d6",
            "defense": "1d6"
        }

class Dragon(Monster):
    """Dragon Monster Class"""

    def __init__(self, subtype, cavern_level, row, col):
        super().__init__(subtype, cavern_level, row, col)
        self._type = "Dragon"
        self._title_a = "Delectable"
        self._title_b = None
        self._drop_a = "Dragon Tail"
        self._drop_b = None
        self._hp = 30
        self._max_hp = 30
        self._dice = {
            "attack": "3d6",
            "defense": "2d6"
        }