items = ["gerbil", "key", "candybars", ]

# gerbil = item("gerbil","There is a weird looking gerbil",False,3,True,"I have the gerbil",0)
# key = item("key","This key looks like it is used for a room",True,1,True,"One blue key",0)
hairpin = item("candy bar","This is one really yummy looking candy bar",True,1,True,"I found a suspicious hairpin",2)
pet_food = item("pet food","This is some gerbil food",False,3,True,"Found some gerbil food",2)
student_list = item("allergy list","These students are allergic to gerbils:<list_students>",True,1,True,"Some students are allergic.",2)
sick_student = item("sick student","This is one really yummy looking candy bar",True,1,True,"A student was sick",2)
absent_student = item("speech therapy","<Name> was at speech therapy",True,1,True,"A student was absent",2)


class item(self,name,description,visible,mutable,notebook,points):
    self.name = name
    self.description = description      ##string
    self.visible = visible              ##boolean
    # self.clue_ranking = clue_ranking    ##0 or 1
    self.mutable = mutable              ##boolean
    self.notebook = notebook            ##string
    self.points = points    ##integer

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class games(self):
    self.name = name
    self.points = points
##tic tac toe
##blackjack
##trivia

title_string =
# def add_to_note_book(self):
#     notebook_list.append(<item>.notebook)