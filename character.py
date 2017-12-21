class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name



class NpcEssential(Character):
    def __init__(self, name, description, interactions, mini_game = None, inventory=[]):
        Character.__init__(self, name, description)
        self.interactions = interactions
        self.inventory = inventory
        self.mini_game = mini_game

    def talk(self):
        return self.interactions_essential[self.name]['game_offer']

    def conclude(self, outcome):
        if outcome:
            print(self.interactions_essential[self.name]['conclusion'])
        else:
            print("Better luck next time!")

    def give(self):
        for item in self.inventory:


class NpcNonEssential(Character):
    def __init__(self, name, description):
        Character.__init__(self, name, description)

    def talk(self):
        print(self.interactions_non_essential[self.name])



class Player(Character):
    def __init__(self, name, description):
        Character.__init__(self, name, description)
        self.notebook = Notebook()
        self.keycard = False
        self.current_loc = hallway[-1]
        self.prev_loc = None

    def move(self, current_room, new_room):
        current_room.inventory.remove(self)
        new_room.inventory.append(self)
        self.prev_loc = self.current_loc
        self.current_loc = new_room

    def log_clue(self, clue):
        self.notebook.write(clue)


if __name__ == '__main__':
    pass

