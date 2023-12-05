class Board:
    def __init__(self):
        # Initialize the 5x5 board
        self._board = [[0 for _ in range(5)] for _ in range(5)]

    def print_board(self):
        for row in self._board:
            print("+--+--+--+--+--+")
            for cell in row:
                print(f"|{str(cell):^2}", end="")
            print("|")
        print("+--+--+--+--+--+")

class Board:
    """Class representing the Santorini game board"""

    def __init__(self):
        self._board_state = [
            [0, 0, 0, 0, 0],
            [0, "0Y", 0, "0B", 0],
            [0, 0, 0, 0, 0],
            [0, "0A", 0, "0Z", 0],
            [0, 0, 0, 0, 0]
        ]

    def display(self):
        """Display the current board state."""
        for row in self._board_state:
            print("+--+--+--+--+--+")
            for cell in row:
                print(f"|{cell}", end=" ")
            print("|")
        print("+--+--+--+--+--+")
