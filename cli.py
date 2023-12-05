import sys

from game import Game
from board import Board

class SantoriniCLI:
    """Driver class for a command-line REPL interface to the Santorini game"""

    def __init__(self):
        self._game = Game()
        self._board = Board()

    def run(self):
        """Start the game with the provided board state."""

        # Display the initial board state
        print(self._board)

        # Perform the first move
        self._perform_move()

    def _perform_move(self):
        """Perform a move in the game."""

        # Get input for worker and direction to move
        worker = input("Select a worker to move\n")
        direction_to_move = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
        direction_to_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")

        # Perform the move
        try:
            self._game.perform_move(worker, direction_to_move, direction_to_build)
        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)

        # Display the updated board state
        self._board.display()

    def _quit(self):
        sys.exit(0)


if __name__ == "__main__":
    try:
        SantoriniCLI().run()
    except Exception as e:
        print("Sorry! Something unexpected happened.")
        sys.exit(0)