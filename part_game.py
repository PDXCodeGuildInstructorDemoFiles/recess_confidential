from noir_items import Item
from noir_rooms import Room
import csv
import os

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
    
        # First 
        for column in readCSV:
            try:
                if column[0] == 'small_room':
                    all_rooms.append(Room(column[1],column[2],column[3]))
                elif column[0] == 'big_room':
                    big_room = Room(column[1], column[2],column[3])
                    for i in all_rooms:
                        big_room.add_room(i)
                    hallway.append(big_room)
                    all_rooms = []
                elif column[0] == 'item':
                    temp_item = Item(column[1],column[2],boolean_check(column[3]),boolean_check(column[4]),column[5],int(column[6]))
                    items.append(temp_item)
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

        for row in readCSV:
            try:
                print(row[0])
            except IndexError:
                continue

    print("")

# Opening story dialogue
def start_dialogue():
    print("It was a sunny afternoon at Central Elementary School.\n")

# Menu interface with Navigating rooms to
def navigation():
    global charlocation

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

        print("\n[H] (Return to Hallway)")

        user = input("Where would you like to go?\n").lower()
        if user == 'h':
            charlocation = hallway
            navigation()
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
        print("\n[H] (Return to {)".format(back_to_room))

        input("Which object do you want to look at?")
        input("")

# Function that returns the class of an object (i.e. room,item,character)
def find_class(new_obj):
    return (new_obj.__class__.__name__)

# Menu Interface
def menu():
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


    log_data()
    charlocation = hallway[-1]
    play_music()
    back_to_room = []

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
            print("Your are in the hallway. \nYou hear a scream and a bloody head rolls out of a classroom. \n")
            input("\n\n\n[Press any key]")

            # loop for continued action select
            while start == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                menu()

        # quits the game
        elif user == 'q':
            quit()