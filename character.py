class Character:
    def __init__(self, name, description, guilt=False):
        self.name = name
        self.description = description
        self.guilt = guilt


class NPC(Character):
    def __init__(self, name, description, guilt=False):
        Character.__init__(self, name, description, guilt)
        self.talk = self.get_dialogue()

    def get_dialogue(self):
        pass

class Player(Character):
    def __init__(self, name, description, guilt=False):
        Character.__init__(self, name, description, guilt)
        self.notebook = Notebook()
        self.keycard = False

    def move(self, current_room, new_room):
        pass

    def start_dialogue(self):
        pass

    def examine_object(self, object):
        pass

    def store_object(self, object):
        pass


if __name__ == '__main__':
    pass





