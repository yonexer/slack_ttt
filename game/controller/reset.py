from helper import *
from game.models.lobby import *

class CtlReset:
    @staticmethod
    def execute(context, params):
        '''
        Command to reset the game, e.g. /ttt reset
        :param context:
        :param params:
        :return:
        '''
        channel_id = context['channel_id']
        reset(channel_id)
        return 'Games cleared. Ready to play.'
