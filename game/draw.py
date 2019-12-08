"""
Draws the board on the screen
"""
from . import board


def draw(new_board):
    if not isinstance(new_board, board.chess_board):
        raise TypeError("Expected {} object, got {} object".format(board.chess_board,
                                                                   type(new_board)))
