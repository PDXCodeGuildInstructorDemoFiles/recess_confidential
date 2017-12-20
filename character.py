class Character:
    def __init__(self, name, description, guilt=False):
        self.name = name
        self.description = description
        self.guilt = guilt
        self.inventory = Inventory()


class NPC(Character):
    def __init__(self, name, description, stats_list, guilt=False):
        Character.__init__(self, name, description, guilt)
        self.stats = stats_list


class Player(Character):
    def __init__(self, name, description, guilt=False):
        Character.__init__(self, name, description, guilt)
        self.stats = self.get_stats()

    def get_stats(self):
        pass


if __name__ == '__main__':
    pass





