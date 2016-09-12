from game.models.game import Game

def test_player1_wins():
    game = Game()
    game.board = [
        [1, 2, 0],
        [1, 2, 0],
        [0, 0, 0]
    ]
    code = game.place(2, 0, 1)
    assert code == 1


def test_player2_wins():
    game = Game()
    game.board = [
        [2, 1, 1],
        [2, 0, 0],
        [0, 0, 0]
    ]
    code = game.place(2, 0, 2)
    assert code == 2


def test_draw():
    game = Game()
    game.board = [
        [1, 1, 2],
        [2, 1, 1],
        [0, 2, 2]
    ]

    code, b = game.place(1, 0, 1)
    assert code == 3

test_player1_wins()
test_player2_wins()
test_draw()