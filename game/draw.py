"""
Draws the board on the screen
"""
from .board import chess_board

def draw(new_board):
    if not isinstance(new_board, chess_board):
        raise TypeError("Expected {} object, got {} object".format(chess_board, type(new_board)))
