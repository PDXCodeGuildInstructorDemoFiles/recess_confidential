# modules
from noir_items import Item
from noir_rooms import Room
from character import Character, NPC, Player
import csv
import os
import urllib

# global vars
notebook = []
hallway = []
items = []
characters = []

# Collects data from Data.csv and creates variables
def log_data():
    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        all_rooms = []
        all_items = []

        for column in readCSV:
            try:
                # imports items
                if column[0] == 'item':
                    temp_item = Item(column[1], column[2], boolean_check(column[3]), boolean_check(column[4]), column[5],int(column[6]))
                    items.append(temp_item)
                    all_items.append(temp_item)
                # imports small rooms first
                elif column[0] == 'small_room':
                    temp_room = Room(column[1],column[2],column[3])
                    for i in range(len(all_items)):
                        temp_room.inventory.append(all_items[i])
                    all_rooms.append(temp_room)
                    all_items = []
                # imports big room after and puts the small rooms in the big room
                elif column[0] == 'big_room':
                    big_room = Room(column[1], column[2],column[3])
                    # loops through the all_rooms list to add to the big room
                    for i in all_rooms:
                        big_room.add_room(i)
                    hallway.append(big_room)
                    all_rooms = []

            except IndexError:
                continue

# Play music function
def play_music():
    from pygame import mixer # Load the required library

    mixer.init()
    mixer.music.load('panther.mp3')
    mixer.music.play()

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


# Menu interface with Navigating rooms to
def navigation():
    global charlocation
    global back_to_room
    global user
    os.system('cls' if os.name == 'nt' else 'clear')

    print(charlocation.description)
    print("")

    # Checks to see if user is in hallway
    if charlocation.size == "1" and charlocation.name == "Hallway":
        print("You are standing in the {}.\n".format(charlocation.name))
        print("You can visit:")
        i = 0
        for key in hallway:
            i += 1
            print("[{}] {}".format(i, key))
        charlocation = hallway[int(input("\nWhere would you like to go?\n"))-1]
        navigation()
    # Checks to see if user is in big rooms (i.e. cafeteria, nurses room,science lab, etc)
    elif charlocation.size == "1":
        print(charlocation.description)
        print("In {} room you can explore:\n".format(charlocation.name))
        for i in range(len(charlocation.connects_to)):
            print("[{}] {}".format(i, charlocation.connects_to[i]))

        print("\n[R]eturn to Hallway")
        print("[M]enu")

        user = input("Where would you like to go?\n").lower()
        if user == 'r':
            charlocation = hallway[-1]
            navigation()
        elif user == 'm':
            menu()
        else:
            user = int(user)
            back_to_room = charlocation
            charlocation = charlocation.connects_to[user]
            navigation()
    # Checks to see if user is in small room (i.e. POIs)
    elif charlocation.size == "0":
        print("\n\nAt {}, you see: ".format(charlocation.name))
        for i in range(len(charlocation.inventory)):
            print("[{}] {}".format(i, charlocation.inventory[i]))

        print("")
        print("\n[R]eturn to {})".format(back_to_room))

        user = input("What would you like to do?")

        if user == 'r':
            charlocation = back_to_room
            navigation()
        elif user == 'm':
            menu()
        else:
            user = int(user)
            back_to_room = charlocation
            if find_class(charlocation.inventory[user]) == "Item":
                print("Item was chosen")
                p_note.write(charlocation.inventory[user])
            elif find_class(charlocation.inventory[user]) == "NPC":
                print("NPC was chosen")
                print("<Insert NPC code commands here>")
                if charlocation.inventory[user].essential
                    if q == 'y':
                        print('TRIVIA GAME')  # here we would run the mini-game module.
                        reward = 1  # this would be returned by the mini-game
                        charlocation.inventory[user].conclude(reward)  # prize or no prize
                        player.notebook.write(charlocation.inventory[user].give())
                    else:
                        print('Ok, see you later.')  # chose not to play
                else:
                    print(charlocation.inventory[user].talk())
            input("")
            navigation()

# Function that returns the class of an object (i.e. room,item,character)
def find_class(new_obj):
    return new_obj.__class__.__name__

# Menu Interface
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(charlocation.description)
    print("")
    print("[C]heck Inventory\n[R]ead Notebook\n[H]elp\n[M]ove\n")
    user = input("What would you like to do?\n").lower()
    if user == 'm':
         navigation()
    elif user == 'r':
        print(notebook)
        input("[PRESS ANY KEY]")

# Init Function
if __name__ == '__main__':
    game = True

    interactions = {
        'Mrs. Frizzle': {'game_offer': 'Would you like to play trivia? ', 'conclusion': 'Ok, here\'s the key.'}}

    science_teacher = NPC('Mrs. Frizzle', 'Frazzled', interactions)

    # print(find_class(science_teacher))
    # q = input(science_teacher.talk()).lower()  # mini-game offer

    log_data()
    charlocation = hallway[-1]
    play_music()
    back_to_room = []

    hallway[2].connects_to[0].inventory.append(science_teacher)

    # runs game
    while game == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        game_start()

        # start or quit select
        user = input("Would you like to:\n" \
                                    "(S)tart a game\n" \
                                    "(Q)uit the game\n" \
                                     ).lower()

        # begins game
        if user == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            start = True

            start_dialogue()

            # loop for continued action select
            while start == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                menu()

        # quits the game
        elif user == 'q':
            quit()