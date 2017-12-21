from noir_items import Item
from noir_rooms import Room
import csv
import os


# from pygame import mixer # Load the required library
#
# mixer.init()
# mixer.music.load('panther.mp3')
# mixer.music.play()

# General Game Functions

def boolean_check(str_bool):
    return True if str_bool == 'True' else False

# Stores Data from Data.csv and creates variables
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    all_rooms = []
    hallway = {}
    items = {}

    for row in readCSV:
        try:
            if row[0] == 'small_room':
                all_rooms.append(Room(row[1],row[2]))
            elif row[0] == 'big_room':
                big_room = Room(row[1], row[2])
                for i in all_rooms:
                    big_room.add_room(i)
                hallway[big_room.name] = big_room
                all_rooms = []
            elif row[0] == 'item':
                temp_item = Item(row[1],row[2],boolean_check(row[3]),boolean_check(row[4]),row[5],int(row[6]))
                items[temp_item.name] = temp_item
        except IndexError:
            continue



if __name__ == '__main__':
    game = True
    round = True
    location = ""
    notebook = []

    while game == True:
        os.system('cls' if os.name == 'nt' else 'clear')

        with open('fun.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')

            for row in readCSV:
                print(row)

        print("----RECESS CONFIDENTIAL----\n")

        user = input("Would you like to:\n" \
                     "(S)tart a game\n" \
                     "(Q)uit the game\n" \
                     ).lower()

        if user == 's':
            while round == True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Your are in a hallway. \nYou hear a scream and a bloody head rolls out of a classroom. \n")
                print("[C]heck Inventory  -- [R]ead Notebook\n")
                print("You see:")
                i = 0
                for key,value in hallway.items():
                    i += 1
                    print("[{}] {}".format(i,key))

                input("Where would you like to go?")





    # for key, value in items.items():
    #     print(key)
    #
    # print(items['Hair pin'].mutable)

# item_chosen = lunchtable.contains()
#
# print(type(hallway['Cafeteria']))
