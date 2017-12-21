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

def player_input():
    letter = ''
    while not (letter == 'x' or letter == 'o'):
        print('Do you want to play as [x] or [o]')
        letter = input().lower
        
        if letter is 'x':
            return ['X', 'O']
        
        elif letter is 'q':
            break
        
        else:
            return ['O', 'X']

def make_move(board, letter, move):
    board[move] = letter

def is_winner(bo, le):
#  Given a board and a player’s letter, this function returns True if that player has won.
#  We use bo instead of board and le instead of letter so we don’t have to type as much.
    return((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left git side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board(board):
    dupeboard = []

    for i in board:
        dupeboard.append(i)
        return dupeboard

def is_freespace(board, move):
    return board[move] == ' '

def get_playermove(board):
    move = '  '
    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not is_freespace(board, int(move)):
        print('What is your next move? [1-9]')
        move = input()
    return int(move)

def get_randommove(board, moveslist):
    c_moves = []
    for i in moveslist:
        if is_freespace(board, i):
            c_moves.append(i)

        if len(c_moves) != 0:
            return random.choice(c_moves)
        else:
            return None

def computer_input(board, computer_ltr):
    if computer_input == 'x':
        player_input = 'O'
    else:
        player_input = 'X'

    for i in range(1, 10):
        copy = get_board(board)
        if is_freespace(copy, i):
            make_move(copy, computer_ltr, i)
            return i
    move = player_input(board[1, 3, 7, 9])
    if move != None:
        return move

    if is_freespace == (board, 5):
        return 5

    return get_randommove(board, [2, 4, 6, 8])
def is_boardfull(board):
    for i in range(1,10):
        if is_freespace(board, i):
            return False
        return True

print('Character Dialogue Welcoming to Tic Tac Toe')

while True:
    the_board = [' '] * 10
    player_input, computer_input = playe0r_input()
    game_play = True

    while game_play is True:
        draw_board(the_board)
        move = get_playermove(the_board)
        make_move(the_board,player_input, move)
        
        if is_winner(the_board, player_input):
            draw_board(the_board)
            print('Character dialogue if player wins')

        else:
            if is_boardfull(the_board):
                draw_board(the_board)
                print('The game is tied')
                break
            else:
                turn = 'computer'

    else:
        move = get_randommove(the_board, computer_input)
        make_move(the_board, computer_input, move)
            
        if is_boardfull(the_board):
            draw_board(the_board)
            print('The computer has beaten you! You lose.')
            game_play = False
        else:
            if is_boardfull(the_board):
                draw_board(the_board)
                print('Player Dialogue for loss')
                break
            else:
                turn = 'player'
    def quit():
        return False

print(player_input())

# tictac_board = draw_board()
