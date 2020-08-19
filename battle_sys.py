import random
from ui_options import *
from player import *
from monster import *

class Battle:
    """Represents a battle encounter for between the Player and the Monster"""
    def __init__(self, Player, Monster):
        """
        Initializes the battle encounter and sets up the battle system components and UI options
        Parameters: Player (object), Monster (object)
        Returns: N/A
        """
        # borders used for UI
        self._border_1 = Table(u'\u2554', u'\u2557', u'\u255a', u'\u255d', u'\u2550', u'\u2551')
        self._border_2 = Table('+', '+', '+', '+', '-', '|')

        self._is_player_alive = True
        self._is_monster_alive = True

        self._player = Player
        self._monster = Monster

        self._hp_limit = Player.get_max_hp()
        self._hp_player = Player.get_hp()
        self._hp_monster = Monster.get_hp()
        self._monster_hp_limit = Monster.get_max_hp()


    def print_encounter_msg(self):
        """
        Prints the encounter message
        Parameters, Returns: N/A
        """
        text = len(self._monster.get_name()) + len("You encounter the ")
        space = (56 - text) // 2

        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
        print(" " * space + "You encounter a " + self._monster.get_name() + "!" + " " * space)
        print(self._border_2.bottom_left + self._border_2.horizontal * 52 + self._border_2.bottom_right)


    def print_battle_menu(self):
        """
        Prints the battle menu with the Player and Monster's HP along with the Player's possible battle actions
        Parameters, Returns: N/A
        """
        space1 = 22 - len(self._player.get_name())
        space2 = 22 - len(self._monster.get_name())

        # print top border
        print(self._border_1.top_left + self._border_1.horizontal * 20, end="")
        print(" < BATTLE > ", end="")
        print(self._border_1.horizontal * 20 + self._border_1.top_right)

        # print Player's and Monster's HP
        if len(str(self._hp_player)) == 2:
            print(self._border_1.vertical + " " * 10 + self._player.get_name() + " " * space1 +
                  "HP: " + str(self._hp_player) + " / " + str(self._hp_limit) + " " * 9 + self._border_1.vertical)
        else:
            print(self._border_1.vertical + " " * 10 + self._player.get_name() + " " * space1 +
                  "HP:  " + str(self._hp_player) + " / " + str(self._hp_limit) + " " * 9 + self._border_1.vertical)

        if len(str(self._hp_monster)) == 2:
            print(self._border_1.vertical + " " * 10 + self._monster.get_name() + " " * space2 +
                  "HP: " + str(self._hp_monster) + " / " + str(self._monster_hp_limit) + " " * 9 + str(self._border_1.vertical))
        else:
            print(self._border_1.vertical + " " * 10 + self._monster.get_name() + " " * space2 +
                  "HP:  " + str(self._hp_monster) + " / " + str(self._monster_hp_limit) + " " * 9 + str(self._border_1.vertical))

        # print Player's battle actions
        print(self._border_1.vertical + self._border_2.horizontal * 52 + self._border_1.vertical)
        print(self._border_1.vertical + " " * 20 + " - Actions -" + " " * 20 + self._border_1.vertical)
        print(self._border_1.vertical + "    [a] - Attack     [d] - Defend     [h] - Heal    " + self._border_1.vertical)

        # print bottom border
        print(self._border_1.bottom_left + self._border_1.horizontal * 52 + self._border_1.bottom_right)


    def attack_dialog(self, battler, opponent, damage):
        """
        Prints dialog when both parties are attacking each other
        Parameters: battler (obj), opponent (obj), damage (int)
        Returns: printed dialog
        """
        if battler == self._player:
            dialog_1 = self._player.get_name() + " " + "attack the" + " " + opponent.get_name() + "!"
            dialog_2 = opponent.get_name() + " " + "takes" + " " + str(damage) + " " + "damage!"

        else:
            dialog_1 = battler.get_name() + " " + "attacks" + "!"
            dialog_2 = opponent.get_name() + " " + "take" + " " + str(damage) + " " + "damage!"

        print(dialog_1)
        print(dialog_2)


    def start_battle(self):
        """
        Loops the battle between Player and Monster object until one's HP value drops to zero
        Parameters: N/A
        Returns:
            True - if Player wins the battle (Monster's HP == 0, Player's HP > 0)
            False - if Player loses the battle (Player's HP == 0, Monster's HP > 0)
        """
        # print encounter message
        self.print_encounter_msg()

        # loop until either the Player or Monster is dead (HP == 0)
        while self._is_player_alive is True and self._is_monster_alive is True:

            player_won = None

            # print battle menu
            self.print_battle_menu()

            # ask Player for battle action input
            player_move = self.player_action(input("What will you do?\n"))

            # get Monster's randomized battle input (attack vs. defend)
            monster_move = self.monster_action()

            if player_move == "attack" and monster_move == "attack":
                player_won = self.case_1()

            elif player_move == "heal":
                player_won = self.case_2(monster_move)

            elif player_move == "defend" or monster_move == "defend" or (player_move == "defend" and monster_move == "defend"):
                player_won = self.case_3(player_move, monster_move)

            # update Player's HP after round of battle
            self._player.set_hp(self._hp_player)

            # if Player won, print message and return back to cavern_cookeries.py
            if player_won is True:
                self._is_monster_alive = False
                return True

            # if Player lost, print message and return back to cavern_cookeries.py
            elif player_won is False:
                self._is_player_alive = False
                return False


    def player_action(self, input):
        """
        Takes Player's input and transforms it into the corresponding battle action
        Parameters: input (str)
        Return: corresponding battle action (str) for valid input
        """
        if input == "a" or input == "A" or input == "attack":
            return "attack"
        elif input == "d" or input == "D" or input == "defend":
            return "defend"
        elif input == "h" or input == "H" or input == "heal":
            return "heal"
        else:
            return


    def monster_action(self):
        """
        Randomly chooses the Monster's battle action of attacking or defending
        Parameters: N/A
        Returns: battle action (str)
        """
        if random.randint(1,2) == 1:
            return "attack"
        else:
            return "defend"


    def case_1(self):
        """
        Battle Case 1 - Both Player and Monster attack each other
        Parameters: N/A
        Returns:
            True - if Player wins (Monster's HP == 0)
            False - if Player loses (PLayer's HP == 0)
            None - if the Player's HP > 0 and Monster's HP > 0
        """
        # generate the Player and Monster's attack damage
        player_attack = self.cast_dice(self._player, "attack")
        monster_attack = self.cast_dice(self._monster, "attack")

        # print top border
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

        # Turn 1 - Player attacks Monster
        # Turn 1 - update Monster's HP, check if Monster is still alive
        self.attack_dialog(self._player, self._monster, player_attack)
        self._hp_monster -= player_attack
        if self._hp_monster <= 0:
            print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
            return True

        # Turn 2 - Monster attacks Player (if Monster is still alive)
        # Turn 2 - update Player's HP and check if Player is still alive
        self.attack_dialog(self._monster, self._player, monster_attack)
        self._hp_player -= monster_attack
        if self._hp_player <= 0:
            print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
            return False

        # print bottom border
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

        # Turn 3 - Player and Monster are both still alive, move onto next round of battle
        # return None


    def case_2(self, monster_action):
        """
        Battle Case 2 - Player heals, Monster attacks or defends
        Parameters: monster_action (str - "attack" or "defend")
        Returns:
            False - if Player loses (PLayer's HP == 0)
            None - if the Player's HP > 0 and Monster's HP > 0
        """
        # print top border
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

        # Turn 1 - restore Player's HP, update HP
        healed_amount = random.randint(10, 15)
        print(self._player.get_name() + " " + "cast heal!")
        print("Restores" + " " + str(healed_amount) + " " + "HP")
        self._hp_player += healed_amount

        # if Player's updated HP is over the max HP limit, will top off at the Player's max HP
        if self._hp_player > self._hp_limit:
            self._hp_player = self._hp_limit

        # Turn 2A - Monster attacks Player
        if monster_action == "attack":
            monster_attack = self.cast_dice(self._monster, "attack")
            self.attack_dialog(self._monster, self._player, monster_attack)

            # Turn 2 - update Player's HP and check if Player is still alive
            self._hp_player -= monster_attack

            if self._hp_player <= 0:
                print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
                return False

        # Turn 2B - Monster defends itself
        else:
            print(self._monster.get_name() + " " + "defends itself!")

        # Turn 3 - Player and Monster are both still alive, move onto next round of battle
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)


    def case_3(self, player_action, monster_action):
        """
        Battle Case 3 - One or both of the battlers defend themselves during the battle
        Parameters: player_action (str - "attack" or "defend"), monster_action (str - "attack" or "defend")
        Returns:
            True - if Player wins (Monster's HP == 0)
            False - if Player loses (PLayer's HP == 0)
            None - if the Player's HP > 0 and Monster's HP > 0
        """
        # print top border
        print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

        # Turn 1A - Player defends themselves
        if player_action == "defend":
            print(self._player.get_name(), "defend yourself!")

            # Turn 2A - Monster defends itself
            if monster_action == "defend":
                print(self._monster.get_name(), "defends itself!")
                # print bottom border
                print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

            # Turn 2B - Monster attacks Player
            else:
                # generate Monster's attack damage and Player's defense damage; Player's defend action will neutralize part or all of the Monster's attack damage
                monster_attack = self.cast_dice(self._monster, "attack")
                player_defense = self.cast_dice(self._player, "defense")

                defended_dmg = monster_attack - player_defense

                if defended_dmg < 0:
                    defended_dmg = 0

                print(self._monster.get_name() + " " + "attacks" + "!")
                print(self._player.get_name(), "take", defended_dmg, "damage!")

                # Turn 2B - update Player's HP and check if Player is still alive
                self._hp_player -= defended_dmg
                if self._hp_player <= 0:
                    print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
                    return False

                print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)

        # Turn 1B - Player attacks
        if player_action == "attack":

            # generate Player's attack damage and Monster's defense damage; Monster's defend action will neutralize part or all of the Player's attack damage
            player_attack = self.cast_dice(self._player, "attack")
            monster_defense = self.cast_dice(self._monster, "defense")

            defended_dmg = player_attack - monster_defense

            if defended_dmg < 0:
                defended_dmg = 0

            print(self._player.get_name() + " " + "attack" + " " + "the" + " " + self._monster.get_name() + "!")
            print(self._monster.get_name(), "defends itself!")
            print(self._monster.get_name(), "takes", defended_dmg, "damage!")

            # Turn 1B - update Monster's HP and check if Monster is still alive
            self._hp_monster -= defended_dmg

            # check if Monster survives
            if self._hp_monster <= 0:
                print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)
                return True

            print(self._border_2.top_left + self._border_2.horizontal * 52 + self._border_2.top_right)


    def cast_dice(self, battler, type):
        """
        Roll the battler's attack or defense dice and return the added value
        Parameters: battler (obj), type (str - "attack" or "defense")
        Returns: Summation of the dice roll(s) (int)
        """
        all_die = battler.get_dice()
        dice = all_die[type]
        # roll the dice and return the result
        result = 0
        for i in range(int(dice[0])):
            result += random.randint(1, int(dice[2]))
        return result
