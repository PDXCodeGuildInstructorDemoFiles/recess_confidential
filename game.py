# modules
from noir_items import Item
from noir_rooms import Room
from notebook import Notebook
import character
import trivia
from notebook import Notebook
import csv
import os
import urllib
import npc_list
from pygame import mixer  # Load the required library for music (pip3 install pygame)


class Game:
    def __init__(self):
        self.locations_list = []
        self.items = []
        self.characters = []
        self.all_rooms = []
        self.all_items = []
        self.player = None
        self.charlocation = None

    def player_setup(self):
        name = input('What is your name? ')
        self.player = character.Player(name, "This is you. You are it!")

    @staticmethod
    def play_music():
        mixer.init()
        mixer.music.load('panther.mp3')
        mixer.music.play()

    @staticmethod
    def str_escape(strng):
        return strng.encode('utf-8').decode("unicode_escape")

    def log_data(self):
        with open('data.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter='|')

            # runs loop to import data with appropriate class and nests data in order of appearance
            for column in readCSV:
                try:
                    # imports items
                    if column[0] == 'item':
                        temp_item = Item(self.str_escape(column[1]), self.str_escape(column[2]),
                                         self.boolean_check(column[3]),
                                         self.boolean_check(column[4]),
                                         self.str_escape(column[5]), int(column[6]))
                        self.items.append(temp_item)
                        all_items.append(temp_item)
                    # imports small rooms first and adds all items before the small room
                    elif column[0] == 'small_room':
                        temp_room = Room(column[1], self.str_escape(column[2]), column[3])
                        for i in range(len(all_items)):
                            temp_room.inventory.append(all_items[i])
                        self.all_rooms.append(temp_room)
                        all_items = []
                    # imports big room after and puts the small rooms in the big room
                    elif column[0] == 'big_room':
                        big_room = Room(column[1], self.str_escape(column[2]), column[3])
                        for i in self.all_rooms:
                            big_room.add_room(i)
                        self.locations_list.append(big_room)
                        self.all_rooms = []

                except IndexError:
                    continue

    @staticmethod
    def boolean_check(str_bool):
        return True if str_bool == 'True' else False

    def __str__(self):
        with open('fun.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            prnt = ''
            # prints each line of the fun.csv file from top to bottom
            for row in readCSV:
                try:
                    prnt += row[0]
                except IndexError:
                    continue
                finally:
                    prnt += '\n '
        return prnt

    @staticmethod
    def start_dialogue():
        print("You are a fourth grade student standing in your Elementary School Hallway during recess.\n")
        print("Just before you were released for recess, your teacher announced that the class gerbil\n")
        print("had gone missing. She was extremely upset by this and threatened the class with detention\n")
        print("for the rest of the week if no one came forward to confess. The bell rang before anyone\n")
        print("could speak, so everyone ran out to the playground. You joined them in the initial sprint\n")
        print("but as you ran out you noticed that no one else seemed to take the situation seriously,\n")
        print("so you take it upon yourself to solve this untimely crime. You need to find out who\n")
        print("who committed the crime, why he or she did it, and bring that information to your teacher\n")
        print("in the classroom by the end of recess. If you fail, everyone in the class will get detention.\n")
        print("If you succeed, only the guilty party will get detention. If you do extremely well, everyone\n")
        print("will get a pizza party (with the exception of the guilty party).")
        input("\n\n\n[PRESS ANY KEY]")

    def score_check(self):
        # NOTE: need to add boolean checks so that actions don't repeat'
        # <if notebook points is greater than num run this code and add dialogue/npc to game>
        if self.player.notebook.points_total()() > 15:
            # Win_condition is a placeholder...replace this with other story related code later
            self.win_condition()()
        elif 15 >= self.player.notebook.points_total()() > 8:
            # placeholder to add thoughts to notebook or add npcs
            print("You are doing ggggggrrrrrrreeeeeat. You think you might know who did it")
            input("")

    @staticmethod
    def find_class(new_obj):
        return new_obj.__class__.__name__

    # Menu interface with Navigating rooms
    def navigation(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.score_check()
        global charlocation
        global user

        print("Current Location: {}\n\n".format(self.charlocation))

        try:
            # Checks to see if user is in hallway
            if self.charlocation.size == "1" and self.charlocation.name == "Hallway":
                print("You are standing in the {}.\n".format(self.charlocation.name))
                print(self.charlocation.description)
                print("\nYou can visit:")
                i = 0
                for key in self.locations_list:
                    i += 1
                    print("[{}] {}".format(i, key))
                print("\n[M]enu")
                q = input("\nWhere would you like to go?\n")
                if q == 'r':
                    self.player.prev_loc = self.charlocation
                    self.charlocation = self.locations_list[-1]
                    self.navigation()
                elif q == 'm':
                    self.menu()
                else:
                    self.player.prev_loc = self.charlocation
                    self.charlocation = self.locations_list[int(q) - 1]
                    self.navigation()
            # Checks to see if user is in big rooms (i.e. cafeteria, nurses room,science lab, etc)
            elif self.charlocation.size == "1" and not self.charlocation.name == "Hallway":
                print(self.charlocation.description)
                print("\nIn the {} room you can explore:\n".format(self.charlocation.name))

                for i in range(len(self.charlocation.connects_to)):
                    print("[{}] {}".format(i + 1, self.charlocation.connects_to[i]))

                print("\n[R]eturn to Hallway")
                print("[M]enu")
                q = input("\nWhere would you like to go?\n").lower()

                if q == 'r':
                    self.player.prev_loc = self.charlocation
                    self.charlocation = self.locations_list[-1]
                    self.navigation()
                elif q == 'm':
                    self.menu()
                else:
                    q = int(q) - 1
                    self.player.prev_loc = self.charlocation
                    self.charlocation = self.charlocation.connects_to[q]
                    self.navigation()

            # Checks to see if user is in small room (i.e. POIs)
            elif self.charlocation.size == "0":
                print(self.charlocation.description)
                print("\n\nAt {}, you see: ".format(self.charlocation.name))
                for i in range(len(self.charlocation.inventory)):
                    print("[{}] {}".format(i + 1, self.charlocation.inventory[i]))

                print("")
                print("\n[R]eturn to {}".format(self.player.prev_loc))
                print("[M]enu")

                q = input("What would you like to do?: ")

                if q == 'r':
                    print(self.player.prev_loc)
                    self.charlocation = self.player.prev_loc
                    self.navigation()
                elif q == 'm':
                    self.menu()
                else:
                    q = int(q) - 1
                    if self.find_class(self.charlocation.inventory[q]) == "Item":
                        # changes variable to choice_item for clarity
                        choice_item = self.charlocation.inventory[q]
                        print("You examine the item:\n")
                        print(choice_item.description)
                        input("")
                        print("\n")
                        self.player.notebook.write(choice_item)
                        self.charlocation.inventory.remove(choice_item)
                    elif self.find_class(self.charlocation.inventory[q]) == "NpcEssential" or self.find_class(
                            self.charlocation.inventory[q]) == "NPCNonEssential":
                        # changes variable to choice_npc for clarity
                        choice_npc = self.charlocation.inventory[q]
                        print("\n")
                        if self.find_class(choice_npc) == "NpcEssential":
                            q = input(choice_npc.talk()).lower()  # mini-game offer
                            if q == 'y':
                                reward = choice_npc.mini_game(
                                    choice_npc.gameparam)  # this would be returned by the mini-game
                                choice_npc.conclude(reward)  # prize or no prize
                                if reward > 0:
                                    self.player.notebook.write(choice_npc.give())
                            else:
                                print('Ok, see you later.')  # chose not to play
                        else:
                            print(choice_npc.talk())
                    input("")
                    self.navigation()
        except ValueError:
            input("That is not a possible choice. Please try again... punk.")
            self.navigation()

    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.score_check()
        print("Current Location: {}\n\n".format(self.charlocation))
        print(self.charlocation.description)
        print("")
        print("[R]ead Notebook\n[H]elp\n[M]ove\n")
        q = input("What would you like to do?\n").lower()

        if q == 'm':
            self.navigation()
        elif q == 'r':
            print(self.player.notebook)
            print("<FOR DEVELOPER>\n Your score is: {}".format(self.player.notebook.points_total()))
            input("[PRESS ANY KEY]")
            self.menu()
        elif q == 'h':
            input("You don't deserve to be helped...")
            self.menu()
        else:
            input("Could not compute...Try again.")

    def play(self):
        print(self)
        self.player_setup()
        print(self.player.name)


g = Game()
g.play()
# print(g.player.name)
