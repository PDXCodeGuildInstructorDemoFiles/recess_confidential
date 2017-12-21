import random

def draw_board(board):
    print('    |    | ')
    print(' ' + board[7] + '|' + board[8] + '|' + board[9])
    print('    |    | ')
    print('---------')
    print('    |    | ')
    print(' ' + board[4] + '|' + board[5] + '|' + board[6])
    print('    |    | ')
    print('---------')
    print('    |    | ')
    print(' ' + board[1] + '|' + board[2] + '|' + board[3])
    print('    |    | ')

def player_input():
    letter = ''
    while not (letter == 'x' or letter == 'o'):
        print('Do you want to play as [x] or [o]')
        letter = input().lower
        if letter is 'x':
            return ['X', 'O']
        else:
            return ['O', 'X']

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
    #top left to bottom right diagnol
    return (bo[7] == le and bo[5] == le and bo[3] == le) or
    #top right to bottom left diagnol
    return (bo[9] == le and bo[5] == le and bo[1] == le) or
    #bottom right to bottom left
    return (bo[1] == le and bo[2] == le and bo[3] == le) or
    #Middle right to middle left
    return (bo[4] == le and bo[5] == le and bo[6] == le) or
    #Top Right to top left
    return (bo[7] == le and bo[8] == le and bo[9] == le) or
    #Top to bottom right
    return (bo[7] == le and bo[4] == le and bo[1] == le) or
    #Top to bottom middle
    return (bo[8] == le and bo[5] == le and bo[2] == le) or
    #Top to bottom left
    return (bo[9] == le and bo[6] == le and bo[3] == le) or
 def get_board(board):
     dupeboard = []

    for i in board:
        dupeboard.append(i)
    return dupeboard


print(player_input())

# tictac_board = draw_board()