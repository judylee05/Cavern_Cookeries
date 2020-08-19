from ui_options import *

class Recipe_Book():
    """Represents the Recipe Book"""

    def __init__(self, player_inventory):
        """Initializes the Recipe Book object"""
        self._border_1 = Table(u'\u2554', u'\u2557', u'\u255a', u'\u255d', u'\u2550', u'\u2551')
        self._border_2 = Table('+', '+', '+', '+', '-', '|')

        self._inventory = set(player_inventory)
        self._recipe_dict = {
            1: {"dish": "Chimera Terrine ", "ingredients": ["Mystery Meat", "Slippery Ooze"],
                "text": "Finely minced chimera meat and strained slime\n ooze combine to create a creamy, attractive\n layered spread perfect for summertime canapes.\n Best served chilled. "},
            2: {"dish": "Dragon Tail Steak ", "ingredients": ["Dragon Tail"],
                "text": "A thick, gamey cut of tail sliced off from the\n legendary dragon that is grilled and seasoned\n with salt and pepper. It’s buttery softness and\n delicious flavors are truly magical. "},
            3: {"dish": "Fruit Jelly ", "ingredients": ["Chewy Gelatin", "Funky Fruit"],
                "text": "This delightfully light and chewy dessert is\n popular with both young and old. Be sure to\n carefully chew each sticky bite – unless\n you wish to visit an early grave."},
            4: {"dish": "Ink Pasta ", "ingredients": ["Chimera Egg", "Giant Tentacle", "Octopus Ink"],
                "text": "The ink gibbers at you when you're not looking,\n but this deliciously garlicky pasta has an amazingly\n rich and silky texture thanks to the chimera eggs.\n Tender tentacles lend this dish a wonderful seafood flavor."},
            5: {"dish": "Monster Medley Hotpot ", "ingredients": ["Chewy Gelatin", "Chimera Egg", "Dragon Tail", "Funky Fruit", "Giant Tentacle", "Mystery Meat", "Octopus Ink", "Slippery Ooze", "Tree Syrup"],
                "text": "A scintillating, possibly venomous mixture of all\n the monsters you've encountered during your adventure,\n lovingly boiled in a spicy soup base. You won't\n be hungry after eating this meal fit for a king."}
        }

    def print_prior_dialog(self):
        """Prints the dialog prior to choosing a dish"""
        text_1 = [
            "With the [Dragon Tail] carefully tucked into your ",
            "bag you hurry back home and leave behind the Cavern.",
            "  ",
            "When you arrive, you find your mentor, Ignis, ",
            "already waiting for you inside. He glances at your",
            "direction but doesn’t leave his seat from the table,",
            "much less smile. Perhaps he's waiting for your meal?",
            "  ",
            "Though you feel the weight of his gaze behind you,",
            "you march into the kitchen and open the ancient ",
            "cook book, eager to prove to him your culinary",
            "skills with the spoils from the Cavern. "
        ]
        self.print_dialog_a(text_1)


    def create_dish(self):
        """Player can cook a meal based on the Monster drops they have in their inventory"""
        unlocked_recipes = []

        self.print_prior_dialog()

        self.print_dialog_a(["MONSTER RECIPES "])

        for key in self._recipe_dict:
            recipe_ingredients = set(self._recipe_dict[key]["ingredients"])

            # if recipe is unlocked, print it out for Player to see
            if recipe_ingredients.issubset(self._inventory):
                dish_title = [str(key) + ". " + "< " + self._recipe_dict[key]["dish"] + ">"]
                self.print_dialog_b(dish_title)
                print(self._recipe_dict[key]["text"])
                unlocked_recipes.append(key)
            else:
                dish_title = [str(key) + ". " + "???"]
                self.print_dialog_b(dish_title)

        chosen_recipe = int(input("Enter the recipe number: "))

        if chosen_recipe in unlocked_recipes:
            self.print_dish_dialog(chosen_recipe)
        else:
            error_text = ["You don't have the necessary ingredients", "Please try again"]
            self.print_dialog_a(error_text)


    def print_dish_dialog(self, recipe_key):
        """Prints the ending dialog after Player successfully creates a dish"""
        text_1 = [
            "After hours of prepping, cooking, and plating ",
            "you present to Ignis your finest dish yet:",
            self._recipe_dict[recipe_key]["dish"]
        ]

        text_2 = [
            "You wait with bated breath as you watch Ignis take",
            "a bite of your dish. It’s been a long day of",
            "exploring dangerous caverns, battling monsters to ",
            "the death, and cooking over a hot stove… but you",
            "feel your exhaustion melt away once you see ",
            "your mentor’s face. ",
            "  ",
            "You see a single tear roll down his face. "
            ]

        text_3 = ["LEVEL UP! You are now a MASTER CHEF!"]

        self.print_dialog_a(text_1)
        self.print_dialog_a(text_2)
        self.print_dialog_a(text_3)


    def print_dialog_a(self, text):
        """Creates a dialog box for text that are even amount of characters each"""
        print(self._border_1.top_left + self._border_1.horizontal * 52 + self._border_1.top_right)

        for i in range(len(text)):
            spacing = (52 - len(text[i])) // 2
            print(self._border_1.vertical + " " * spacing + text[i] + " " * spacing + self._border_1.vertical)

        print(self._border_1.bottom_left + self._border_1.horizontal * 52 + self._border_1.bottom_right)


    def print_dialog_b(self, text):
        """Creates a dialog box with no vertical border - only top and bottom"""
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

        for i in range(len(text)):
            spacing = (54 - len(text[i])) // 2
            print(" " * spacing + text[i] + " " * spacing)

        print(self._border_2.bottom_left + self._border_2.horizontal * 52 + self._border_2.bottom_right)

