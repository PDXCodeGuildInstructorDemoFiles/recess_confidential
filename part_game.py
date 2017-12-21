from noir_items import Item
from noir_rooms import Room
import csv
import os

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

def play_music():
    from pygame import mixer # Load the required library

    mixer.init()
    mixer.music.load('panther.mp3')
    mixer.music.play()

# General Game Functions

def boolean_check(str_bool):
    return True if str_bool == 'True' else False

def game_start():
    with open('fun.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            try:
                print(row[0])
            except IndexError:
                continue

    print("")


def start_dialogue():
    print("It was a sunny afternoon at Central Elementary School.\n")

def navigation():
    global charlocation
    if charlocation.size == "1" and charlocation.name == "Hallway":
        print("You are standing in the hallway.\n")
        print("You can visit:")
        i = 0
        for key in hallway:
            i += 1
            print("[{}] {}".format(i, key))
        charlocation = hallway[int(input("\nWhere would you like to go?\n"))-1]
        navigation()
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
    elif charlocation.size == "0":
        print("\n\nAt {}, you see: ".format(charlocation.name))
        for i in range(len(charlocation.inventory)):
            print("[{}] {}".format(i, charlocation.inventory[i]))
        print("")
        print("\n[H] (Return to {)".format(back_to_room))

        input("Which object do you want to look at?")
        input("")


def find_class(new_obj):
    print(new_obj.__class__.__name__)

def menu():
    print("[C]heck Inventory\n[R]ead Notebook\n[H]elp\n[M]ove\n")
    user = input("What would you like to do?\n").lower()
    if user == 'm':
         navigation()
    elif user == 'r':
        print(notebook)
        input("[PRESS ANY KEY]")




if __name__ == '__main__':
    game = True


    log_data()
    play_music()
    charlocation = hallway[-1]
    back_to_room = []


    while game == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        game_start()
        print(hallway)
        user = input("Would you like to:\n" \
                                    "(S)tart a game\n" \
                                    "(Q)uit the game\n" \
                                     ).lower()

        if user == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            start = True

            start_dialogue()
            print("Your are in the hallway. \nYou hear a scream and a bloody head rolls out of a classroom. \n")
            input("\n\n\n[Press any key]")

            while start == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                menu()

        elif user == 'q':
            quit()


