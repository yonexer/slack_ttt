from helper import *
from game.models.lobby import *

class CtlNewGame:
    @staticmethod
    def execute(context, params):
        '''
        The command to start a new game, e.g. /ttt play-with @hliu
        :param context:
        :param params:
        :return:
        '''
        channel_id = context['channel_id']
        player1 = context['player']
        player2 = params[0]
        if player2[0] != '@':
            raise Exception('Please specify the player name with @')
        player2 = player2[1:]
        if player1 == player2:
            raise Exception('You cannot play with yourself!')
        game = get_game(channel_id)

        if has_ongoing_game(game):
            raise Exception('Please wait')

        new_game(channel_id, player1, player2)

        return 'New game started: ' + player1 + ' vs ' + player2 + '\n'
