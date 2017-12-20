# big_rooms_dict = [classroom, teacherdesk,student1desk,chalkboard,trashcan]
#                   [gym,bleachers,fountain,room3,room4]
#                   [lockerroom,locker1,locker2,trashcan,bench]
#                   [cafeteria, lunchline,lunchtable,doorway,kitchen]
#                   [gym,swings,monkeybars,bballcourt]
#                   [principal office, princdesk,shelf1,shelf2]

move_count = 0
start_point = "classroom"



class Room:

    def __init__(self, name, description):
        self.name = name
        self.description = description  ##string
        self.inventory = []  ##list[item (or) character]
        self.open_req = []
        self.connects_to = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def move_to(self):
        self.move_count = self.move_distance + 1


classroom = Room("Class Room 10b","There is an empty classroom with a chalkboard and desks.")
teacherdesk = Room("Teacher's Desk","There is a teacher's desk by the chalkboard")
studentdesk = Room("Jack's Desk","Jack's desk has a deck of cards resting on it")

big_classroom = [classroom,teacherdesk, studentdesk]


print("You have entered {}. You can see {} and {}".format(big_classroom[0],big_classroom[1],big_classroom[2]))