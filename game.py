import csv


class Game:
    def __init__(self):
        pass

    def set_up(self):
        pass


# Stores Data from Data.csv and creates variables
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    all_rooms = []
    hallway = {}
    items = {}

if __name__ == "__main__":
    game = Game()
