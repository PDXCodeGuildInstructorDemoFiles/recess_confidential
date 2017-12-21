# Stores Data from Data.csv and creates variables
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    all_rooms = []
    hallway = {}
    items = {}

    for row in readCSV:
        try:
            # if row[0] == 'small_room':
            #     all_rooms.append(Room(row[1],row[2]))
            # # elif row[0] == 'big_room':
            # #     big_room = Room(row[1], row[2])
            # #     for i in all_rooms:
            # #         big_room.add_room(i)
            # #     hallway[big_room.name] = big_room
            # #     all_rooms = []
            # # # elif row[0] == 'item':
            # # #     temp_item = Item(row[1],row[2],boolean_check(row[3]),boolean_check(row[4]),row[5],int(row[6]))
            # # #     items[temp_item.name] = temp_item
        except IndexError:
            continue