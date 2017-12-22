
# Tic Tac Toe
import random


def draw_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def get_board(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)
    return dupe_board


def is_spacefree(board, move):
    return board[move] == ' '


def player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_spacefree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def c_movelist(board, movesList):
    possible_moves = []
    for i in movesList:
        if is_spacefree(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def c_move(board, c_letter):
    if c_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in range(1, 10):
        copy = get_board(board)
        if is_spacefree(copy, i):
            make_move(copy, c_letter, i)
            if is_winner(copy, c_letter):
                return i

    for i in range(1, 10):
        copy = get_board(board)
    if is_spacefree(copy, i):
        make_move(copy, player_letter, i)
        if is_winner(copy, player_letter):
            return i

    move = c_movelist(board, [1, 3, 7, 9])
    if move != None:
        return move

    if is_spacefree(board, 5):
        return 5

    return c_movelist(board, [2, 4, 6, 8])


def is_boardfull(board):
    for i in range(1, 10):
        if is_spacefree(board, i):
            return False
    return True


print('Intro dialogue')

while True:
    the_board = [' '] * 10
    player_letter, c_letter = player_letter()
    turn = 'player'
    print('The ' + turn + ' will go first.')
    is_playing = True

    while is_playing:
        if turn == 'player':
            draw_board(the_board)
            move = player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('NPC loss dialogue.')
                is_playing = False

            else:
                if is_boardfull(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = c_move(the_board, c_letter)
            make_move(the_board, c_letter, move)

            if is_winner(the_board, c_letter):
                draw_board(the_board)
                print('Player loss dialogue.')
                is_playing = False
            else:
                if is_boardfull(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not play_again():
        break
