from noir_items import Item


class Notebook:
    def __init__(self):
        self.data = []

    def write(self, item):
        print("You inspect {}.\n\nInteresting Find!\n...You examine the item and add the item to your notepad...".format(item))
        self.data.append(item)

    def __str__(self):
        clues = []
        for x in self.data:
            clues.append('{}: {}'.format(x.name, x.description))
        print('You have collected the following clues in your detective\'s notebook:')
        return '\n'.join(clues)

    def points_total(self):
        total = 0
        for x in self.data:
            total += x.points
        return total


if __name__ == '__main__':
    p_note = Notebook()
    apple = Item('apple', 'a red delicious apple', True, False, 'whatever', 2)
    calendar = Item('calendar', 'a wall calendar', True, False, 'whatever', 3)

    p_note.write(apple)
    p_note.write(calendar)

    print(p_note)
    print(p_note.points_total())
