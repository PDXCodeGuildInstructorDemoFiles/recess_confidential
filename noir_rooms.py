rooms = ["classroom", "gym", "locker room", "cafeteria", "playground", "principal's office"]

move_count = 0
start_point = "classroom"

class rooms:
    self.description = description      ##string
    self.inventory = inventory
    self.doors = doors
    self.open_req = open_req            ##(list[rooms])
    self.move_count = move_count        ##integer
    self.trigger = trigger
    def move_to(self):
        self.move_count = move_count + 1
