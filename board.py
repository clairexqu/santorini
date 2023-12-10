from cell import Cell
from coordinate import Coordinate

class Board:
    """Class representing the Santorini game board"""

    def __init__(self):
        self._board = [[Cell(0, ' ') for col in range(5)] for row in range(5)]
        self.winner_worker = None

        # correct positions 
        
        self.workers = {
            "A": Coordinate(3, 1),
            "B": Coordinate(1, 3),
            "Y": Coordinate(1, 1),
            "Z": Coordinate(3, 3)}

        # checks winning by height of 3 
        #self._board[2][2] = Cell(3, ' ')
        #self._board[3][1] = Cell(2, 'A')

        # checks winning by if player can't move 
        # self.workers = {
        #     "A": Coordinate(3, 1),
        #     "B": Coordinate(1, 3),
        #     "Y": Coordinate(0, 0),
        #     "Z": Coordinate(0, 1)}
        # self._board[1][0] = Cell(2, ' ')
        # self._board[1][1] = Cell(2, ' ')
        # self._board[1][2] = Cell(2, ' ')
        # self._board[0][2] = Cell(2, ' ')
        
        self.set_worker_start_position()

    def worker_on_three(self):
        #print("worker on 3 called\n")
        for worker, coordinate in self.workers.items():
            cell = self.get_cell(coordinate.row, coordinate.column) 
            if cell.height == 3:
                self.winner_worker = worker
            
    # def both_workers_stuck(self):


    def set_worker_start_position(self):
        for worker, coordinate in self.workers.items():
            self.update_cell(coordinate, worker, 0)

    def execute_turn(self, turn):
        worker = turn.worker
        # remove worker from old cell
        self.update_cell(self.workers[worker], " ", 0)
        # add worker to new cell
        self.update_cell(turn.placement_coordinate, worker, 0)
        # edit the original coordinate dict
        self.workers[turn.worker] = turn.placement_coordinate
        # adding 1 to build cell 
        self.update_cell(turn.build_coordinate," ", 1)

        # checks to see if a worker won
        self.worker_on_three()

    def update_cell(self, coordinate, new_char, height_add):
        cell = self.get_cell(coordinate.row, coordinate.column)
        cell.worker_character = new_char
        cell.height += height_add

    def get_cell(self, row, column):
        return self._board[row][column]
        
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