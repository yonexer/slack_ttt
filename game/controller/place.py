from helper import *
from game.models.lobby import *

class CtlPlace:
    @staticmethod
    def execute(context, params):
        '''
        Command to place a piece, e.g. /ttt place 0 0
        :param context:
        :param params:
        :return:
        '''
        channel_id = context['channel_id']
        player = context['player']
        x = int(params[0])
        y = int(params[1])

        if not is_in_board(x, y):
            raise Exception('Out of board.')

        game = get_game(channel_id)
        if not has_ongoing_game(game):
            raise Exception('There is no game now. Please start a new one.')

        code = place(game, channel_id, player, x, y)

        if code in [Game.CODE_PLAYER1_WIN, Game.CODE_PLAYER2_WIN]:
            game.delete()
            return 'Player ' + player + ' wins. '

        if code == Game.CODE_DRAW:
            game.delete()
            return 'Draw'

        if code == Game.CODE_POSITION_TAKE:
            raise Exception('The position is unavailable')

        return print_board(game)
