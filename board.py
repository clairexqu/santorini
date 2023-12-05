from cell import Cell

class Board:
    """Class representing the Santorini game board"""

    def __init__(self):
        self._board = [[Cell(0, ' ') for col in range(5)] for row in range(5)]
        
        # replace these 
        self._board[3][1] = Cell(0, 'A')
        self._board[1][3] = Cell(0, 'B')
        
        self._board[1][1] = Cell(0, 'Y')
        self._board[3][3] = Cell(0, 'Z')

    def __str__(self):
        """Return the current board state."""
        board_str = ""
        for row in self._board:
            board_str += "+--+--+--+--+--+\n"
            for cell in row:
                board_str += f"|{str(cell)}"
            board_str += "|\n"
        board_str += "+--+--+--+--+--+"
        
        return board_str

