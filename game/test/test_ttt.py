from game.models.game import Game

def test_game_should_return_1_if_player1_wins():
    board = [
        [1, 2, 0],
        [1, 2, 0],
        [0, 0, 0]
    ]
    game = Game()
    code, b = game.place(board, 2, 0, 1)
    assert code == 1


def test_game_should_return_2_if_player2_wins():
    board = [
        [2, 1, 1],
        [2, 0, 0],
        [0, 0, 0]
    ]
    game = Game()
    code, b = game.place(board, 2, 0, 2)
    assert code == 2


def test_game_should_return_3_if_tie():
    board = [
        [1, 1, 2],
        [2, 1, 1],
        [0, 2, 2]
    ]
    game = Game()
    code, b = game.place(board, 2, 0, 1)
    assert code == 3

test_game_should_return_1_if_player1_wins()
test_game_should_return_2_if_player2_wins()
test_game_should_return_3_if_tie()