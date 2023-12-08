from cell import Cell
from coordinate import Coordinate

class Board:
    """Class representing the Santorini game board"""

    def __init__(self):
        self._board = [[Cell(0, ' ') for col in range(5)] for row in range(5)]

        self.workers = {
            "A": Coordinate(3, 1),
            "B": Coordinate(1, 3),
            "Y": Coordinate(1, 1),
            "Z": Coordinate(3, 3)}
        
        self.set_worker_start_position()
    
    def set_worker_start_position(self):
        #print("HERE\n\n")
        for worker, coordinate in self.workers.items():
            self.update_cell(coordinate.row, coordinate.column, worker)

    def move_worker(self, worker_char, move):
        pass
        #update_cell()
        #update_cell()

    def update_cell(self, row, column, char):
        self._board[row][column].worker_character = char
    

        
        # replace these 
        # self._board[3][1] = Cell(0, 'A')
        # self._board[1][3] = Cell(0, 'B')
        
        # self._board[1][1] = Cell(0, 'Y')
        # self._board[3][3] = Cell(0, 'Z')

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
