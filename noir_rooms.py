big_rooms_dict = [classroom, teacherdesk,student1desk,chalkboard,trashcan]
                  [gym,bleachers,fountain,room3,room4]
                  [lockerroom,locker1,locker2,trashcan,bench]
                  [cafeteria, lunchline,lunchtable,doorway,kitchen]
                  [gym,swings,monkeybars,bballcourt]
                  [principal office, princdesk,shelf1,shelf2]

move_count = 0
start_point = "classroom"

classroom = room(classroom,"There is an empty classroom with a chalkboard and desks.", None)
teacherdesk = room(teacherdesk,"There is a teacher's desk by the chalkboard", classroom)

json reader


class room(self,name,description,big_room):
    self.name = name
    self.description = description      ##string
    self.inventory = inventory          ##list[item (or) character]
    self.connects_to = big_room         ##list[rooms]
    self.open_req = []

          ##dict{item: text, item:text}

    # self.move_distance = move_distance  ##integer
    # self.trigger = trigger              ##string

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def move_to(self):
        self.move_count = self.move_distance + 1