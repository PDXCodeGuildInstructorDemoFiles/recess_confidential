class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class NpcEssential(Character):
    def __init__(self, name, description, interactions, mini_game=None):
        Character.__init__(self, name, description)
        self.interactions = interactions
        self.inventory = []
        self.mini_game = mini_game

    def talk(self):
        return self.interactions[self.name]['game_offer']

    def conclude(self, outcome):
        if outcome:
            print(self.interactions[self.name]['conclusion'])
        else:
            print("Better luck next time!")

    def give(self):
        return self.inventory.pop()


class NpcNonEssential(Character):
    def __init__(self, name, description,interactions):
        Character.__init__(self, name, description)
        self.interactions = interactions

    def talk(self):
        print(self.interactions[self.name])



class Player(Character):
    def __init__(self, name, description):
        Character.__init__(self, name, description)
        self.notebook = Notebook()
        self.keycard = self.check_keycard()
        self.current_loc = hallway[-1]
        self.prev_loc = None

    def move(self, current_room, new_room):
        current_room.inventory.remove(self)
        new_room.inventory.append(self)
        self.prev_loc = self.current_loc
        self.current_loc = new_room

    def log_clue(self, clue):
        self.notebook.write(clue)

    def check_keycard(self):
        if keycard in self.notebook:
            return True
        return False


if __name__ == '__main__':
    pass

