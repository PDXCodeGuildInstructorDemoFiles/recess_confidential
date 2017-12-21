class Room:
    move_choice = -1

    def __init__(self, name, description,size):
        self.name = name
        # self.description = description.replace('\n', r'\n')  ##code to try and add escape keys...doesnt work
        self.description = description
        self.size = size
        self.inventory = []  ##list[item (or) character]
        self.open_req = []
        self.connects_to = []

    # code that uses name to be shown as the object
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    # adds the rooms that are connected to this room
    def add_room(self,room):
        self.connects_to.append(room)

    # move calculate function (not implemented yet)
    def move_to(self):
        self.move_count = self.move_distance + 1

# Old code to add rooms
# classroom = Room("Class Room 10b","There is an empty classroom with a chalkboard and desks.")
# teacherdesk = Room("Teacher's Desk","There is a teacher's desk by the chalkboard")
# studentdesk = Room("Jack's Desk","Jack's desk has a deck of cards resting on it")
#
# cafeteria = Room("Cafeteria","There is a messy cafeteria")
# lunchtable = Room("Lunch Table","There is a half eaten slice of pizza on the table")
# blackjackkids = Room("Black Jack Table","There are a lot of kids playing blackjack")
#
# classroom.add_room(teacherdesk)
# classroom.add_room(studentdesk)
#
# cafeteria.add_room(lunchtable)
# cafeteria.add_room(blackjackkids)
#
# lunchtable.inventory.append("Book")
# lunchtable.inventory.append("Box")
#
#
# print("You have entered {}. You can see {}".format(classroom.name,classroom.connects_to))
#
# print("You have selected {}".format(classroom.connects_to[classroom.print_choices()]))
#
#
# print("You have selected {}".format(classroom.connects_to[cafeteria.print_choices()]))
#
# lunchtable.contains()