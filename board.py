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