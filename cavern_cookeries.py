from ui_options import *
from battle_sys import *
from recipe_book import *
from player import *
from monster import *

class Cavern:
    """Represents the Cavern object that the Player will explore"""

    def __init__(self):
        """Initializes the Cavern with 3 levels"""
        self._border_0 = Table(u'\u250c', u'\u2510', u'\u2514', u'\u2518', u'\u2500', u'\u2502')
        self._border_1 = Table(u'\u2554', u'\u2557', u'\u255a', u'\u255d', u'\u2550', u'\u2551')
        self._border_2 = Table('+', '+', '+', '+', '-', '|')

        # cavern height and width will be equal
        self._c_height = 15
        self._c_width = 15
        self._current_level = 1
        self._cavern_template = [[""] * self._c_width for i in range(self._c_height)]
        self._total_caverns = dict()
        self._player = []
        # inventory of Monster objects in each level
        self._monster_lv1 = []
        self._monster_lv2 = []
        self._monster_lv3 = []
        self.setup_cavern()
        self._game_state = "UNFINISHED"


    def start_game(self):
        """Play the Cavern Cookeries game"""
        self.print_start_screen()

        while self._game_state == "UNFINISHED":
            self.print_map()
            self.receive_input()


    def setup_cavern(self):
        """
        Setup the Cavern maps by parsing the txt files' map layouts for each Cavern level
        Creates the Player object once Player's location has been found in the level_1.txt
        """
        file_content = ""
        cavern_level = 1
        counter = 0

        # need to manually change how many txt files will be looped
        txt_files_list = ["level_1.txt", "level_2.txt", "level_3.txt"]

        # parse each map's contents
        for txt in txt_files_list:
            with open(txt, "r") as infile:
                for line in infile:
                    file_content += line.strip()

            for x in range(self._c_width):
                for y in range(self._c_height):
                    space = file_content[counter]

                    # look for Player indicated on level_1.txt ("@")
                    if space == "@":
                        self._player = Player(1, x, y)
                        file_space = file_content[counter]
                        self._cavern_template[x][y] = file_space
                        counter += 1
                    else:
                        file_space = file_content[counter]
                        self._cavern_template[x][y] = file_space
                        counter += 1

            self._total_caverns[cavern_level] = self._cavern_template
            cavern_level += 1

            # clear variables for the next map level to be loaded
            counter = 0
            file_content = ""
            self._cavern_template = [[""] * self._c_width for i in range(self._c_height)]

        # add in the monsters in each level
        self.add_monster(Slime, "a", 1, 2, 4)
        self.add_monster(Treant, "a", 1, 8, 10)
        self.add_monster(Chimera, "a", 1, 8, 3)
        self.add_monster(Octopus, "a", 1, 12, 9)
        self.add_monster(Slime, "b", 2, 9, 3)
        self.add_monster(Treant, "b", 2, 12, 13)
        self.add_monster(Chimera, "b", 2, 9, 10)
        self.add_monster(Octopus, "b", 2, 6, 5)
        self.add_monster(Dragon, "a", 3, 7, 7)


    def print_start_screen(self):
        """Prints the title art and opening dialog"""

        title_art = [ "█▀▀ ▄▀█ █░█ █▀▀ █▀█ █▄░█   █▀▀ █▀█ █▀█ █▄▀ █▀▀ █▀█ █ █▀▀ █▀",
                      "█▄▄ █▀█ ▀▄▀ ██▄ █▀▄ █░▀█   █▄▄ █▄█ █▄█ █░█ ██▄ █▀▄ █ ██▄ ▄█"]

        for line in title_art:
            print(line)

        opening_dialog = [
            "After a long, perilous journey, the gaping maw",
            "of the Cavern lies before you. It's said to be",
            "home to a legendary dragon sleeping atop a hoard",
            "of wealth so grand it could make a king weep",
            "with envy. But that's not what you're here for -",
            "instead, your goal is to defeat the dragon, ",
            "bring back its delicious meat, and impress",
            "your mentor with a truly wonderful dish in order",
            "to become a Master Chef worthy of the title.",
            "  ",
            "Between you and your goal, however, lies a long ",
            "road full of dangerous monsters...",
            "Dangerous, delicious monsters.",
            "  ",
            "Armed with your trusty cooking utensils and ",
            "an ancient recipe book (that led you here in",
            "the first place), you set foot into the dark",
            "cave, eager to demonstrate to the world your",
            "culinary prowess! "
        ]

        self.print_dialog_a(opening_dialog)


    def print_map(self):
        """Prints the current cavern map that the player is on, based on self._current_level"""
        total_menu = [
            "[w] - up",
            "[s] - down",
            "[a] - left",
            "[d] - right",
            self._border_1.horizontal * 7 + " < STATUS > " + self._border_1.horizontal * 6,
            "HP: " + str(self._player.get_hp()) + "/" + str(self._player.get_max_hp()),
            self._border_1.horizontal * 5 + " < INVENTORY > " + self._border_1.horizontal * 5]

        # for scenario where there's nothing in inventory
        if len(self._player.get_inventory()) == 0:
            total_menu.append("None")
        else:
            for item in self._player.get_inventory():
                total_menu.append(item)

        # print top border
        print(self._border_1.top_left + self._border_1.horizontal * 3, end="")
        print("  Cavern Level: ", self._current_level, " ", end="")
        print(self._border_1.horizontal * 10, end="")
        print(" < CONTROLS > ", end="")
        print(self._border_1.horizontal * 5 + self._border_1.top_right)

        for x in range(self._c_width):
            # add the vertical left border + space between border / map
            print(self._border_1.vertical, " " * 4, end="")

            for y in range(self._c_height):
                # get cavern map information from the current level
                cavern_map = self._total_caverns[self._current_level]
                space = cavern_map[x][y]
                print(space, end="")

                # print border between left (map) and right (controls/status/inventory) part of the layout
                if y == self._c_width - 1:
                    print(" " * 4, self._border_1.vertical, end="")

                    # print the menu information line by line
                    for i in range(len(total_menu)):
                        if x == i and x != 5:
                            space = 24 - len(total_menu[i]) + 1
                            print(" " + total_menu[i] + " " * space + self._border_1.vertical, end="")

                        if x == i and x == 5:
                            if len(str(self._player.get_hp())) == 2:
                                space = 24 - len(total_menu[i]) + 1
                                print(" " + total_menu[i] + " " * space + self._border_1.vertical, end="")
                            else:
                                hp_text = ["HP:  " + str(self._player.get_hp()) + "/" + str(self._player.get_max_hp())]
                                space = 24 - len(hp_text[0]) + 1
                                print(" " + hp_text[0] + " " * space + self._border_1.vertical, end="")

                    # for when there's a missing item in the inventory
                    if len(total_menu) != self._c_width:
                        for j in range(len(total_menu), 16):
                            if x == j:
                                print(" " * 26 + self._border_1.vertical, end="")
            print()

        # print bottom border
        print(self._border_1.bottom_left + self._border_1.horizontal * 52 + self._border_1.bottom_right)


    def print_dialog_a(self, text):
        """Creates a dialog box for text that have an even amount of characters"""
        print(self._border_1.top_left + self._border_1.horizontal * 52 + self._border_1.top_right)
        for i in range(len(text)):
            spacing = (52 - len(text[i])) // 2
            print(self._border_1.vertical + " " * spacing + text[i] + " " * spacing + self._border_1.vertical)
        print(self._border_1.bottom_left + self._border_1.horizontal * 52 + self._border_1.bottom_right)


    def print_dialog_b(self, text):
        """Creates a dialog box for text that have an odd amount of characters"""
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
        for i in range(len(text)):
            spacing = (54 - len(text[i])) // 2
            print(" " * spacing + text[i] + " " * spacing)
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)


    def add_monster(self, monster_type, subtype, cavern_level, row, col):
        """Adds a Monster object into a Cavern level map"""
        monster = monster_type(subtype, cavern_level, row, col)

        map = self._total_caverns[cavern_level]
        map[row][col] = monster

        # update total_caverns dict()
        self._total_caverns[cavern_level] = map

        # add monster to monster_location list
        if cavern_level == 1:
            self._monster_lv1.append(monster)
        elif cavern_level == 2:
            self._monster_lv2.append(monster)
        else:
            self._monster_lv3.append(monster)


    def delete_monster(self, row, col):
        """Deletes the Monster object from the Cavern level map after it is defeated in battle"""
        # remove the Monster object from the cavern map by changing it to a blank space (" ")
        map = self._total_caverns[self._current_level]
        map[row][col] = " "

        # remove the Monster object from the list of monsters for that cavern level
        if self._current_level == 1:
            monster_list = self._monster_lv1
        elif self._current_level == 2:
            monster_list = self._monster_lv2
        else:
            monster_list = self._monster_lv3

        new_list = []

        # iterate through the list of monsters on the current floor and add the non-deleted one into a new list
        for entry in monster_list:
            if [self._current_level, row, col] != entry.get_location():
                new_list.append(entry)

        # replace the current monster list with a new list
        if self._current_level == 1:
            self._monster_lv1 = new_list
        elif self._current_level == 2:
            self._monster_lv2 = new_list
        else:
            self._monster_lv3 = new_list


    def move_player(self, new_row, new_col):
        """Move the Player on the Cavern level map"""
        map = self._total_caverns[self._current_level]

        # delete the "C" character on the map and move it to the new location
        player_loc = self._player.get_location()

        map[player_loc[1]][player_loc[2]] = " "
        map[new_row][new_col] = "@"

        # change Player object's location
        self._player.set_location(self._current_level, new_row, new_col)


    def move_next_level(self, row, col):
        """Move the Player to the next Cavern level after Player climbs up a ladder"""
        # change the current level by +1 in order to display the next level's map
        self._current_level += 1

        text = ["You move onto the next level"]
        self.print_dialog_a(text)

        # add the player onto the new map and update the Player object's location
        map = self._total_caverns[self._current_level]
        map[row][col] = "@"
        self._player.set_location(self._current_level, row, col)


    def receive_input(self):
        """Receives the Player's input from the Cavern level map"""
        print("Input your movement:")
        player_input = input()
        map = self._total_caverns[self._current_level]
        player_location = self._player.get_location()
        player_row = player_location[1]
        player_col = player_location[2]

        # move upwards
        if player_input == "w":
            player_row -= 1
        # move downwards
        elif player_input == "s":
            player_row += 1
        # move left
        elif player_input == "a":
            player_col -= 1
        # move right
        elif player_input == "d":
            player_col += 1
        # if player makes an invalid selection, will print an error message
        else:
            text = ["Please enter a valid input"]
            self.print_dialog_a(text)
            return

        space = map[player_row][player_col]

        # if player hits a wall, print error message and restart
        if space == "#":
            text = ["You hit a wall"]
            self.print_dialog_a(text)
            return

        # if the player moves to an empty space, move the player
        elif space == " ":
            self.move_player(player_row, player_col)

        # if the player steps on a ladder, move the player to the next level
        elif space == "^":
            self.move_next_level(player_row, player_col)

        # if the player encounters a monster, engage in battle!
        else:
            # create new battle instance with the Player object and Monster object on the current space
            battle = Battle(self._player, space)
            battling_dragon = False

            if space.get_type() == "Dragon":
                battling_dragon = True

            if battle.start_battle() is True:
                # print dialog box
                text = ["You defeated the " + space.get_name() + "!", "You obtain a " + "[" + space.get_drop() + "]"]
                self.print_dialog_b(text)

                # place Monster drop into Player's inventory
                self._player.add_inventory(space.get_drop())

                # delete Monster from map and __init__ list
                self.delete_monster(player_row, player_col)
                self.move_player(player_row, player_col)

                # if the dragon was defeated, then will move onto cooking
                if battling_dragon is True:

                    total_recipes = Recipe_Book(self._player.get_inventory())
                    total_recipes.create_dish()

                    # change game state and stop the game
                    self._game_state = "FINISHED"



            # if Player gets defeated in battle
            else:
                text_a = ["With no more health left, you decide to flee... "]
                self.print_dialog_a(text_a)

                print(self._border_1.top_left + self._border_1.horizontal * 52 + self._border_1.top_right)
                print(self._border_1.vertical + " " * 21 + "GAME OVER " + " " * 21 + self._border_1.vertical)
                print(self._border_1.bottom_left + self._border_1.horizontal * 52 + self._border_1.bottom_right)

                # change game state and stop the game
                self._game_state = "FINISHED"


if __name__ == '__main__':

    my_game = Cavern()
    my_game.start_game()