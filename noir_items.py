

class Item:
    def __init__(self, name, description,visible,mutable,notebook,points):
        self.name = name
        self.description = description      ##string
        self.visible = visible              ##boolean
        self.mutable = mutable              ##boolean
        self.notebook = notebook            ##string
        self.points = points    ##integer

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# items = ["gerbil", "key", "candybars", ]

# gerbil = item("gerbil","There is a weird looking gerbil",False,3,True,"I have the gerbil",0)
# key = item("key","This key looks like it is used for a room",True,1,True,"One blue key",0)


# class games(self):
#     self.name = name
#     self.points = points
##tic tac toe
##blackjack
##trivia
#
# hairpin = Item("Hair pin","This is one really yummy looking candy bar",True,True,"I found a suspicious hairpin",2)
# pet_food = Item("pet food","This is some gerbil food",False,True,"Found some gerbil food",2)
# student_list = Item("allergy list","These students are allergic to gerbils:<list_students>",True,True,"Some students are allergic.",2)
# sick_student = Item("sick student","This is one really yummy looking candy bar",True,True,"A student was sick",2)
# absent_student = Item("speech therapy","<Name> was at speech therapy",True,True,"A student was absent",2)

# print("Inspecting...")
# time.sleep(2)
# if print_choices == 1:
# ##describe item and add to inventory
# elif print_choices == 0:
# ##play game module
# else:
#     print("Please Try Again")

# def add_to_note_book(self):
#     notebook_list.append(<item>.notebook)