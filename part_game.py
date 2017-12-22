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
# from pygame import mixer # Load the required library for music (pip3 install pygame)

# Collects data from Data.csv and creates variables
def log_data():
    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        all_rooms = []
        all_items = []

        # runs loop to import data with appropriate class and nests data in order of appearance
        for column in readCSV:
            try:
                # imports items
                if column[0] == 'item':
                    temp_item = Item(column[1], column[2], boolean_check(column[3]), boolean_check(column[4]),
                                     column[5], int(column[6]))
                    items.append(temp_item)
                    all_items.append(temp_item)
                # imports small rooms first and adds all items before the small room
                elif column[0] == 'small_room':
                    temp_room = Room(column[1], column[2], column[3])
                    for i in range(len(all_items)):
                        temp_room.inventory.append(all_items[i])
                    all_rooms.append(temp_room)
                    all_items = []
                # imports big room after and puts the small rooms in the big room
                elif column[0] == 'big_room':
                    big_room = Room(column[1], column[2], column[3])
                    for i in all_rooms:
                        big_room.add_room(i)
                    locations_list.append(big_room)
                    all_rooms = []

            except IndexError:
                continue

# Play music function
# def play_music():
    
# #     mixer.init()
# #     mixer.music.load('panther.mp3')
# #     mixer.music.play()

# Converts string of "True" to Boolean of <True>
def boolean_check(str_bool):
    return True if str_bool == 'True' else False

# Loads the ASCII graphics from fun.csv
def game_start():
    with open('fun.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        # prints each line of the fun.csv file from top to bottom
        for row in readCSV:
            try:
                print(row[0])
            except IndexError:
                continue
    print("")

# Opening story dialogue
def start_dialogue():
    print("It was a sunny afternoon at Central Elementary School.\n")
    print("Your are in the hallway. \nYou hear a scream and a bloody head rolls out of a classroom. \n")
    input("\n\n\n[PRESS ANY KEY]")

# Menu interface with Navigating rooms
def navigation():
    os.system('cls' if os.name == 'nt' else 'clear')
    score_check()
    global charlocation
    global back_to_room
    global user

    print("Current Location: {}\n\n".format(charlocation))

    try:
        # Checks to see if user is in hallway
        if charlocation.size == "1" and charlocation.name == "Hallway":
            print("You are standing in the {}.\n".format(charlocation.name))
            print(charlocation.description)
            print("\nYou can visit:")
            i = 0
            for key in locations_list:
                i += 1
                print("[{}] {}".format(i, key))
            print("\n[M]enu")
            q = input("\nWhere would you like to go?\n")
            if q == 'r':
                back_to_room = charlocation
                charlocation = locations_list[-1]
                navigation()
            elif q == 'm':
                menu()
            else:
                back_to_room = charlocation
                charlocation = locations_list[int(q) - 1]
                navigation()
        # Checks to see if user is in big rooms (i.e. cafeteria, nurses room,science lab, etc)
        elif charlocation.size == "1" and not charlocation.name == "Hallway":
            print(charlocation.description)
            print("In {} room you can explore:\n".format(charlocation.name))

            for i in range(len(charlocation.connects_to)):
                print("[{}] {}".format(i+1, charlocation.connects_to[i]))

            print("\n[R]eturn to Hallway")
            print("[M]enu")
            q = input("\nWhere would you like to go?\n").lower()

            if q == 'r':
                back_to_room = charlocation
                charlocation = locations_list[-1]
                navigation()
            elif q == 'm':
                menu()
            else:
                q = int(q) - 1
                back_to_room = charlocation
                charlocation = charlocation.connects_to[q]
                navigation()

        # Checks to see if user is in small room (i.e. POIs)
        elif charlocation.size == "0":
            print("\n\nAt {}, you see: ".format(charlocation.name))
            for i in range(len(charlocation.inventory)):
                print("[{}] {}".format(i+1, charlocation.inventory[i]))

            print("")
            print("\n[R]eturn to {}".format(back_to_room))
            print("[M]enu")

            q = input("What would you like to do?: ")

            if q == 'r':
                print(back_to_room)
                charlocation = back_to_room
                navigation()
            elif q == 'm':
                menu()
            else:
                q = int(q) - 1
                if find_class(charlocation.inventory[q]) == "Item":
                    # changes variable to choice_item for clarity
                    choice_item = charlocation.inventory[q]
                    print("\n")
                    p_note.write(choice_item)
                    charlocation.inventory.remove(choice_item)
                elif find_class(charlocation.inventory[q]) == "NpcEssential" or find_class(charlocation.inventory[q]) == "NPCNonEssential":
                    # changes variable to choice_npc for clarity
                    choice_npc = charlocation.inventory[q]
                    print("\n")
                    if find_class(choice_npc) == "NpcEssential":
                        q = input(choice_npc.talk()).lower()  # mini-game offer
                        if q == 'y':
                            reward = choice_npc.mini_game(choice_npc.gameparam)  # this would be returned by the mini-game
                            choice_npc.conclude(reward)  # prize or no prize
                            if reward > 0:
                                p_note.write(choice_npc.give())
                        else:
                            print('Ok, see you later.')  # chose not to play
                    else:
                        print(choice_npc.talk())
                input("")
                navigation()
    except ValueError:
        input("That is not a possible choice. Please try again... punk.")
        navigation()

# Function that returns the class of an object (i.e. room,item,character)
def find_class(new_obj):
    return new_obj.__class__.__name__

# Menu Interface
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    score_check()
    print("Current Location: {}\n\n".format(charlocation))
    print(charlocation.description)
    print("")
    print("[R]ead Notebook\n[H]elp\n[M]ove\n")
    q = input("What would you like to do?\n").lower()

    if q == 'm':
        navigation()
    elif q == 'r':
        print(p_note)
        print("<FOR DEVELOPER>\n Your score is: {}".format(p_note.points_total()))
        input("[PRESS ANY KEY]")
        menu()
    elif q == 'h':
        input("You don't deserve to be helped...")
        menu()
    else:
        input("Could not compute...Try again.")

def score_check():
    # NOTE: need to add boolean checks so that actions don't repeat'
    # <if notebook points is greater than num run this code and add dialogue/npc to game>
    if p_note.points_total() > 15:
        # Win_condition is a placeholder...replace this with other story related code later
        win_condition()
    elif 15 >= p_note.points_total() > 8:
        # placeholder to add thoughts to notebook or add npcs
        print("You are doing ggggggrrrrrrreeeeeat. You think you might know who did it")
        input("")

def win_condition():
    print("Congratulations. You won!!!")
    input("...")
    quit()

# Init Function
if __name__ == '__main__':
    game = True

    # Imports data, creates global vars, and substantiates objects
    notebook = []
    locations_list = []
    items = []
    characters = []

    log_data()
    player = character.Player("Conan", "This is you. You are it!")
    charlocation = locations_list[-1]
    back_to_room = []
    p_note = Notebook()
    # Appends NPC to small rooms
    clue01 = Item("Red's ultimate clue","Red heard that the girl took care of the gerbil last week",False,False,"sketch PETA girl",4)
    clue02 = Item("Ms Frizzle ultimate clue","Bad student kid thing is allergic yo",False,False,"not bad dude",6)
    npc_list.red_mcguffin.inventory.append(clue01)
    npc_list.ms_frizzle.inventory.append(clue02)
    locations_list[2].connects_to[0].inventory.append(npc_list.ms_frizzle)
    locations_list[0].connects_to[1].inventory.append(npc_list.red_mcguffin)
    locations_list[4].connects_to[0].inventory.append(npc_list.ned_beasley)

    # runs game
    while game:
        os.system('cls' if os.name == 'nt' else 'clear')
        game_start()

        print(npc_list.ms_frizzle.interactions)
        # start or quit select
        q = input("Would you like to:\n" \
                     "(S)tart a game\n" \
                     "(Q)uit the game\n" \
                     ).lower()

        # begins game
        if q == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            start = True
            start_dialogue()

            # loop for continued action select
            while start:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                menu()

        # quits the game
        elif q == 'q':
            quit()