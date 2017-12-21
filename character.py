class Character:
    def __init__(self, name, description, guilt=False):
        self.name = name
        self.description = description
        self.guilt = guilt


class NPC(Character):
    def __init__(self, name, description, interactions, guilt=False):
        Character.__init__(self, name, description, guilt)
        self.interactions = interactions

    def talk(self):
        return self.interactions[self.name]['game_offer']

    def conclude(self, outcome):
        if outcome:
            print(self.interactions[self.name]['conclusion'])
        else:
            print("Better luck next time!")


class Player(Character):
    def __init__(self, name, description, guilt=False):
        Character.__init__(self, name, description, guilt)
        # self.notebook = Notebook()
        self.keycard = False
        self.current_loc = hallway[-1]
        self.prev_loc = None

    def move(self, current_room, new_room):
        current_room.inventory.remove(self)
        new_room.inventory.append(self)
        self.prev_loc = self.current_loc
        self.current_loc = new_room

    def examine_object(self, object):
        pass

    def store_object(self, object):
        pass


if __name__ == '__main__':
    pass

