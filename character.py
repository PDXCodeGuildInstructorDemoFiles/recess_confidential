from notebook import Notebook


class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class NpcEssential(Character):
    def __init__(self, name, description, interactions, mini_game=None, gameparam=None):
        Character.__init__(self, name, description)
        self.interactions = interactions
        self.inventory = []
        self.mini_game = mini_game
        self.gameparam = gameparam
        self.games_played = 0

    def talk(self):
        return self.interactions[self.name]['game_offer']

    def conclude(self, outcome):
        if outcome:
            print(self.interactions[self.name]['conclusion'])
        else:
            print("Better luck next time!")

    def set_reward_value(self):
        for x in self.inventory:
            if self.games_played == 0:
                x.points = 5
            elif self.games_played == 1:
                x.points = 3
            else:
                x.points = 2

    def give(self):
        return self.inventory.pop()


class NpcNonEssential(Character):
    def __init__(self, name, description, interactions):
        Character.__init__(self, name, description)
        self.interactions = interactions

    def talk(self):
        print(self.interactions[self.name])


class Player(Character):
    def __init__(self, name, description):
        Character.__init__(self, name, description)
        self.notebook = Notebook()
        self.hall_pass = self.check_hall_pass()
        self.current_loc = None
        self.prev_loc = []

    def move(self, current_room, new_room):
        current_room.inventory.remove(self)
        new_room.inventory.append(self)
        self.prev_loc = self.current_loc
        self.current_loc = new_room

    def log_clue(self, clue):
        self.notebook.write(clue)

    def check_hall_pass(self):
        for x in self.notebook.data:
            if x.name == 'hall pass':
                return True
            return False


if __name__ == '__main__':
    pass
