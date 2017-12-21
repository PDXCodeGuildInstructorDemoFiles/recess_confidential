from noir_items import Item
from character import *


class Notebook:
    def __init__(self):
        self.data = []

    def write(self, item):
        self.data.append(item)

    def __str__(self):
        clues = []
        for x in self.data:
            clues.append('{}: {}. {}.'.format(x.name, x.description, x.notebook))
        print('You have collected the following clues in your detective\'s notebook:')
        return '\n'.join(clues)

    def points_total(self):
        total = 0
        for x in self.data:
            total += x.points
        return total


if __name__ == '__main__':
    p_note = Notebook()
    apple = Item('apple', 'a red delicious apple', True, False, 'seems suspicious', 2)
    calendar = Item('calendar', 'a wall calendar', True, False, 'november 3rd is circled', 3)

    p_note.write(apple)
    teacher = NpcEssential('Mrs. Frizzle', 'Frazzled', {'hi'})
    teacher.inventory.append(calendar)

    print(p_note)
    print(p_note.points_total())

    p_note.write(teacher.give())

    print(p_note)
    print(p_note.points_total())
