from board import BLANKSQUARE

def modify_board(boardstate: list, start_square: int, end_square: int):
    """
    Function that modifies the board and returns the modified board.
    """

    board = boardstate[:]

    piece = board[start_square]

    board[start_square] = BLANKSQUARE
    board[end_square] = piece

    return board