
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

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def play_again():
     # This function returns True if the player wants to play again, otherwise it returns False.
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')

def make_move(board, letter, move):
     board[move] = letter

def is_winner(bo, le):
      # Given a board and a player’s letter, this function returns True if that player has won.
      # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def get_board(board):
     # Make a duplicate of the board list and return it the duplicate
    dupe_board = []

    for i in board:
        dupe_board.append(i)
    return dupe_board

def is_spacefree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def player_move(board):
     # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_spacefree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def c_movelist(board, movesList):
     # Returns a valid move from the passed list on the passed board.
     # Returns None if there is no valid move.
    possible_moves = []
    for i in movesList:
        if is_spacefree(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None

def c_move(board, c_letter):
     # Given a board and the computer's letter, determine where to move and return that move.
    if c_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

     # Here is our algorithm for our Tic Tac Toe AI:
     # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board(board)
        if is_spacefree(copy, i):
            make_move(copy, c_letter, i)
            if is_winner(copy, c_letter):
                return i

     # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = get_board(board)
    if is_spacefree(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

     # Try to take one of the corners, if they are free.
    move = c_movelist(board, [1, 3, 7, 9])
    if move != None:
        return move

     # Try to take the center, if it is free.
    if is_spacefree(board, 5):
        return 5

     # Move on one of the sides.
    return c_movelist(board, [2, 4, 6, 8])

def is_boardfull(board):
     # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if is_spacefree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
     # Reset the board
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
                print('Hooray! You have won the game!')
                is_playing = False
                is_winner = True
            else:
                if is_boardfull(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
             # Computer’s turn.
            move = c_move(the_board, c_letter)
            make_move(the_board, c_letter, move)

            if is_winner(the_board, c_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
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