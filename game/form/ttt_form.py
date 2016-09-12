from django import forms
from game.controller.place import CtlPlace
from game.controller.current import CtlCurrent
from game.controller.new_game import CtlNewGame
from game.controller.reset import CtlReset
import traceback

class TTTForm(forms.Form):
    '''
    This is the Slack form
    '''
    channel_id = forms.CharField(max_length=255)
    text = forms.CharField(max_length=255)
    user_name = forms.CharField(max_length=255)

    CMD_PLAY = 'play-with'
    CMD_PLACE = 'place'
    CMD_CURRENT = 'current'
    CMD_RESET = 'reset'
    CMD_HELP = 'help'

    def process(self):
        '''
        form process
        :return:
        '''
        channel_id = self.cleaned_data['channel_id'].replace(' ', '')
        text = self.cleaned_data['text']
        user_name = self.cleaned_data['user_name'].replace(' ', '')

        context = {
            'player': user_name,
            'channel_id': channel_id,
        }

        try:
            # parse
            inputs = self._parse(text)
            cmd = inputs[0]
            params = inputs[1:]

            # execute it
            ret = None
            if cmd == self.CMD_PLAY:
                ret = CtlNewGame.execute(context, params)
            elif cmd == self.CMD_PLACE:
                ret = CtlPlace.execute(context, params)
            elif cmd == self.CMD_CURRENT:
                ret = CtlCurrent.execute(context, None)
            elif cmd == self.CMD_RESET:
                ret = CtlReset.execute(context, None)
            elif cmd == self.CMD_HELP:
                ret = self._help()
            return str(ret)
        except Exception as e:
            traceback.print_exc()
            return e.message + '\n' + self._help()

    def _parse(self, text):
        '''
        parse the text from the slack custom command
        :param text:
        :return:
        '''
        inputs = [t.replace(' ', '') for t in text.split(' ')]
        inputs = [t.lower() for t in inputs if not not t]
        if len(inputs) == 0:
            raise Exception('')
        cmd = inputs[0]
        if not cmd in [self.CMD_PLAY, self.CMD_PLACE, self.CMD_CURRENT, self.CMD_RESET, self.CMD_HELP]:
            raise Exception('Unsupported command: ' + cmd)
        # make sure each cmd has the correct options
        self._validate(cmd, inputs[1:])
        return inputs

    def _validate(self, cmd, options):
        '''
        validate the command
        :param cmd:
        :param options:
        :return:
        '''
        if cmd == self.CMD_PLAY:
            assert len(options) == 1, "Please specify the other player"
        elif cmd == self.CMD_PLACE:
            assert len(options) == 2, "Please specify the location"
        elif cmd == self.CMD_CURRENT:
            assert len(options) == 0, "No params"
        elif cmd == self.CMD_RESET:
            assert len(options) == 0, "No params"
        elif cmd == self.CMD_HELP:
            assert len(options) == 0, "No params"

    def _help(self):
        return """
/ttt play-with @player - Start a new game with user. e.g. /ttt play-with @hliu
/ttt current - The current game
/ttt place x y - Place a piece  at (x y). x y => [0, 3).
/ttt help - Show this help page.
/ttt reset - Stop the ongoing game.
        """

