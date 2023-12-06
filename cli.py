import sys

#from game import Game
from board import Board

class SantoriniCLI:
    """Driver class for a command-line REPL interface to the Santorini game"""

    def __init__(self):
        #self._game = Game()
        self._board = Board()

    def run(self):
        """Start the game with the provided board state."""

# eventually should be while not self._board.is_game_over():
        while True:

            # Display the initial board state
            print(str(self._board))

        #sys.exit(0)
        
            # Perform the first move
            self._create_move()

    def _create_move(self):
        """Perform a move in the game."""

        # Get input for worker and direction to move

        worker = input("Select a worker to move\n")
        move_direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
        build_direction = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")

        print(f"{worker},{move_direction},{build_direction}")

        # player_move = Move(worker, move_direction, build_direction)
        # # Perform the move
        # try:
        #     self._game.perform_move(player_move)
        # except Exception as e:
        #     print(f"Error: {str(e)}")
        #     sys.exit(1)

        # Display the updated board state
        # self._board.display()

    def _quit(self):
        sys.exit(0)

class Move:
    def __init__(self, worker, move_direction, build_direction):
        self._worker = worker
        self._move_direction = move_direction
        self._build_direction = build_direction
    
    
if __name__ == "__main__":
    try:
        SantoriniCLI().run()
    except Exception as e:
        print("Sorry! Something unexpected happened.")
        sys.exit(0)