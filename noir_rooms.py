# big_rooms_dict = [classroom, teacherdesk,student1desk,chalkboard,trashcan]
#                   [gym,bleachers,fountain,room3,room4]
#                   [lockerroom,locker1,locker2,trashcan,bench]
#                   [cafeteria, lunchline,lunchtable,doorway,kitchen]
#                   [gym,swings,monkeybars,bballcourt]
#                   [principal office, princdesk,shelf1,shelf2]

move_count = 0
start_point = "classroom"



class Room:

    def __init__(self, name, description,inventory):
        self.name = name
        self.description = description  ##string
        self.inventory = inventory  ##list[item (or) character]
        self.open_req = []
        self.connects_to = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def move_to(self):
        self.move_count = self.move_distance + 1


classroom = Room("Class Room 10b","There is an empty classroom with a chalkboard and desks.", None)
teacherdesk = Room("Teacher's Desk","There is a teacher's desk by the chalkboard", classroom)

print(classroom.name)