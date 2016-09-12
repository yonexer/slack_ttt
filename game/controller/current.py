from helper import *
from game.models.lobby import *

class CtlCurrent:
    @staticmethod
    def execute(context, params):
        '''
        The current command, e.g. /ttt current
        :param context:
        :param params:
        :return:
        '''
        channel_id = context['channel_id']
        game = get_game(channel_id)
        if not has_ongoing_game(game):
            raise Exception('There is no ongoing game now. Please create one first.')
        return print_board(game)

