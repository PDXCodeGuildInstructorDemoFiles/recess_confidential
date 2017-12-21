from noir_items import Item


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
   pass
