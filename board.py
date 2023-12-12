from cell import Cell
from coordinate import Coordinate


class Board:
    """Class representing the Santorini game board consisting of a 2d list of cells,
    the winning worker (None if no one has won), and a dictionary of the workers and their coordinates
    """

    def __init__(self):
        self._board = [[Cell(0, " ") for col in range(5)] for row in range(5)]
        self.winner_worker = None
        self.workers = {
            "A": Coordinate(3, 1),
            "B": Coordinate(1, 3),
            "Y": Coordinate(1, 1),
            "Z": Coordinate(3, 3),
        }
        self._set_worker_start_position()

    def _worker_on_three(self):
        # checks to see if any workers are in a cell of height 3 and sets winner_worker to that worker char
        for worker, coordinate in self.workers.items():
            cell = self.get_cell(coordinate.row, coordinate.column)
            if cell.height == 3:
                self.winner_worker = worker

    def _set_worker_start_position(self):
        # sets workers on the board when the board is first created
        for worker, coordinate in self.workers.items():
            self._update_cell(coordinate, worker, 0)

    def execute_turn(self, turn):
        """executes the turn on a board (a placement and a build)"""
        worker = turn.worker
        # remove worker from old cell
        self._update_cell(self.workers[worker], " ", 0)
        # add worker to new cell
        self._update_cell(turn.placement_coordinate, worker, 0)
        # edit the worker dict to have the new coordinate
        self.workers[turn.worker] = turn.placement_coordinate
        # adding 1 to build cell
        self._update_cell(turn.build_coordinate, " ", 1)

        # checks to see if a worker won
        self._worker_on_three()

    def _update_cell(self, coordinate, new_char, height_add):
        # updates a cell at a particular coordinate with a char and adds a value to its height (0 or 1)
        cell = self.get_cell(coordinate.row, coordinate.column)
        cell.worker_character = new_char
        cell.height += height_add

    def get_cell(self, row, column):
        """returns a cell at a particular row and column of a board"""
        return self._board[row][column]

    def __str__(self):
        """Return a string representing the current board state."""
        board_str = ""
        for row in self._board:
            board_str += "+--+--+--+--+--+\n"
            for cell in row:
                board_str += f"|{str(cell)}"
            board_str += "|\n"
        board_str += "+--+--+--+--+--+"
        return board_str


# FINAL DRAFT
