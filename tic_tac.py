class Board:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.layout = self.make_board(row,col)

    def make_board(self,row,col):
        board_layout = []
        lines = []
        for r in range(row):
            for c in range(col):
                lines.append("-")
            board_layout.append(lines)
            lines = []
        return board_layout

    def place_token(self,r,c,player):
        self.layout[r][c]=player

    def print_board(self):
        for r in range(self.row):
            for c in range(self.col):
                print(self.layout[r][c],end="|")
            print("")

    def calc_winner(self,player):

        # Horizontal
        for r in range(self.row):
                # If Finds Player value, trigger horizontal search
                if self.layout[r][0] == player:
                    win_score = 0
                    for check in range(self.col):
                        if self.layout[r][check] == player:
                            win_score += 1
                            if win_score == self.col:
                                return "{} WINS".format(player)
                        elif self.layout[r][check] != player:
                            win_score = 0
                            break
                    win_score = 0

        # Vertical
        for c in range(self.col):
                # If Finds Player value, trigger vertical search
                if self.layout[0][c] == player:
                    win_score = 0
                    for check in range(self.row):
                        if self.layout[check][c] == player:
                            win_score += 1
                            if win_score == self.col:
                                return "{} WINS".format(player)
                                win_score = 0
                        elif self.layout[check][c] != player:
                            win_score = 0
                            break
                    win_score = 0

        # Diagonal Down
        win_score = 0
        if self.layout[0][0] == player:
            for diag in range(self.col):
                if self.layout[diag][diag] == player:
                    win_score +=1
                    if win_score == self.col:
                        return "{} WINS".format(player)
                        win_score = 0
                else:
                    win_score = 0
                    break

        # Diag Up
        win_score = 0
        if self.layout[self.row -1][0] == player:
            for diag in range(self.col):
                if self.layout[self.row-diag-1][diag] == player:
                    win_score +=1
                    if win_score == self.col:
                        return "{} WINS".format(player)
                        win_score = 0
                else:
                    win_score = 0
                    break




tictac = Board(3,3)

tictac.place_token(input('pick a row: '),input('pick a colomn: '),"x")
tictac.print_board()

tictac.place_token(input('pick a row'),input('pick a colomn'),"x")

tictac.place_token(input('pick a row'),input('pick a colomn'),"x")

tictac.place_token(input('pick a row'),input('pick a colomn'),"x")




print(tictac.calc_winner("x"))

# _rows = [
#     [None, None, 'x'],
#     ['', 'X', ''],
#     [' ', ' ', 'O'],
# ]
#
# _coord_to_token = {
#     (0, 0): 'X',
#     'a1': 'O',
#     '02': None,
# }
#
# _token_coords = [
#     (1, 1, 'X'),
#     (0, 1, 'O'),
# ]