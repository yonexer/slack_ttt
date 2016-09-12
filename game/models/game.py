from django.db import models

class Game(models.Model):

    class Meta:
        app_label = 'slack_ttt'
        db_table = "game"

    # db model
    game_id = models.AutoField(primary_key=True, auto_created=True)
    channel_id = models.CharField(max_length=127, unique=True, null=False, default='')
    player1 = models.CharField(max_length=127, null=False, default='')
    player2 = models.CharField(max_length=127, null=False, default='')
    last_player = models.CharField(max_length=127, null=False, default='')
    board = models.CharField(max_length=255, null=False, default='')

    CODE_POSITION_TAKE = -1
    CODE_CONTINUE = 0
    CODE_PLAYER1_WIN = 1
    CODE_PLAYER2_WIN = 2
    CODE_DRAW = 3

    PLAYER_1 = 1
    PLAYER_2 = 2

    def next_player(self):
        '''
        who is the next player
        :return: the next player's name
        '''
        if self.last_player == '':
            return 'anyone'
        next_player_user_name = self.player1 if self.last_player == self.player2 else self.player2
        return next_player_user_name

    def is_player_in_game(self, channel_id, player):
        '''
        Check if the player is in the channel
        :param channel_id:
        :param player:
        :return: boolean
        '''
        if self.channel_id == channel_id and player in [self.player1, self.player2]:
            return True
        return False

    def is_current_player_turn(self, player):
        '''
        Am I the truen?
        :param player:
        :return: boolean
        '''
        if len(self.last_player) == 0:
            return True
        return self.last_player != player

    def place(self, player, x, y):
        '''
        Place a piece
        :param player:
        :param x: int
        :param y: int
        :return: int
        '''
        n = 3

        if self.board[x][y] != 0:
            return self.CODE_POSITION_TAKE

        self.board[x][y] = player
        self.last_player = self.player1 if player == self.PLAYER_1 else self.player2
        self.save()

        for i in range(n):
            if (self.board[i][0] != 0 and
                        self.board[i][0] == self.board[i][1] and
                        self.board[i][1] == self.board[i][2]):
                return player
            if (self.board[0][i] != 0 and
                        self.board[0][i] == self.board[1][i] and
                        self.board[1][i] == self.board[2][i]):
                return player
        if (self.board[0][0] == self.board[1][1] and
                    self.board[1][1] == self.board[2][2] and
                    self.board[0][0] != 0):
            return player
        if (self.board[0][2] == self.board[1][1] and
                    self.board[1][1] == self.board[2][0] and
                    self.board[0][2] != 0):
            return player

        draw = True
        for i in range(n):
            for j in range(n):
                if self.board[i][j] == 0:
                    draw = False
                    break
        if draw:
            return self.CODE_DRAW

        # continue the game
        return self.CODE_CONTINUE