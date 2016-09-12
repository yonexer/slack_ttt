from game.models.lobby import *

def has_ongoing_game(game):
    return not not game

def print_board(game):
    if not isinstance(game.board, list):
        game.board = load_board(game.board)
    ret = '|---+---+---|\n'
    for i in range(3):
        ret += '|'
        for j in range(3):
            if game.board[i][j] == 1:
                ret += ' O |'
            elif game.board[i][j] == 2:
                ret += '  X  |'
            else:
                ret += '     |'
        ret += '\n|---+---+---|\n'
    return 'Current:\n' + str(ret) + ' \n Legends\n "O": ' + game.player1 + '\n "X": ' + game.player2 + \
                '.\n\nThe next move should be done by player: ' + game.next_player()

def is_in_board(i, j):
    return 0 <= i < 3 and 0 <= j < 3

