from game import Game
import ast

def get_game(channel_id):
    '''
    Find the game
    :param channel_id:
    :return: the game or null
    '''
    games = Game.objects.filter(channel_id__iexact=channel_id)[:1]  # limit = 1
    if len(games) > 0:
        return games[0]
    return None

def load_board(board_db):
    '''
    load from db
    :param board_db:
    :return:
    '''
    return ast.literal_eval(board_db)

def new_game(channel_id, player1, player2):
    '''
    new game
    :param channel_id: int
    :param player1: str
    :param player2: str
    :return: void
    '''
    game = Game()
    game.channel_id = channel_id
    game.player1 = player1
    game.player2 = player2
    game.last_player = ''
    game.board = [[0 for j in range(3)] for i in range(3)]
    game.save()

def reset(channel_id):
    '''
    reset the current game
    :param channel_id: int
    :return: void
    '''
    game = get_game(channel_id)
    if not game:
        raise Exception('No game right now')
    game.delete()

def place(game, channel_id, player, x, y):
    '''
    place a piece
    :param game: game
    :param channel_id: int
    :param player: int, current player
    :param x: int
    :param y: int
    :return: int
    '''
    if game and not game.is_player_in_game(channel_id, player):
        raise Exception('You are not allowed to play in this game')

    if not game.is_current_player_turn(player):
        raise Exception(
            'Please wait for the other player ' + game.next_player())

    if player == game.player1:
        player = Game.PLAYER_1
    else:
        player = Game.PLAYER_2

    game.board = load_board(game.board)
    code = game.place(player, x, y)

    return code