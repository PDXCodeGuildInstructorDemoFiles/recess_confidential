items = ["gerbil", "key", "candybars", ]

gerbil = item("gerbil","There is a weird looking gerbil",False,3,True,"I have the gerbil",1)
key = item("key","This key looks like it is used for a room",True,1,True,"One blue key",1)
candybar = item("candy bar","This is one really yummy looking candy bar",True,1,True,"A candy bar",1)

class item(self,name,description,visible,clue_ranking,mutable,notebook,space_amount):
    self.description = description      ##string
    self.visible = visible              ##boolean
    self.clue_ranking = clue_ranking    ##0 or 1
    self.mutable = mutable              ##boolean
    self.notebook = notebook            ##string
    self.space_amount = space_amount    ##integer

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# def add_to_note_book(self):
#     notebook_list.append(<item>.notebook)