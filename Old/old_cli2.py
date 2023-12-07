import sys
import abc
from game import Game

#CONVERTING THIS TO GAME 

class StateCLI(metaclass=abc.ABCMeta):
    """Base class for game states."""
    @abc.abstractmethod
    def handle_input(self, game):
        raise NotImplementedError()
    
    @abc.abstractmethod
    def update(self, game):
        raise NotImplementedError()

class PickPieceState(StateCLI):
    """State representing the movement phase."""

    def handle_input(self, game):
        worker = input("Select a worker to move: ")

    def update(self, game):
        if game.is_game_over():
            game.set_state(GameOverState())

class PlacementState(StateCLI):
    """State representing the worker placement phase."""

    def handle_input(self, game):
        position = input("Select a position to place the worker (row column): ")
        #game.place_worker(worker, row, col)

    def update(self, game):
        if game.is_placement_complete():
            game.set_state(BuildingState())


class BuildingState(StateCLI):
    """State representing the building phase."""

    def handle_input(self, game):
        position = input("Select a position to build (row column): ")
        game.build_level(row, col)

    def update(self, game):
        if game.is_building_complete():
            game.set_state(MovementState())

class GameOverState(StateCLI):
    """State representing the game over phase."""

    def handle_input(self, game):
        choice = input("The game is over. Would you like to play another game? (yes/no): ")
        if choice.lower() == "yes":
            game.reset()
            game.set_state(PlacementState())
        else:
            sys.exit(0)

    def update(self, game):
        pass

    def set_state(self, state):
        self._state = state

    def run(self):
        """Start the game with the provided board state."""
        print(str(self._board))
        self._state.handle_input(self)
        self._state.update(self)

class SantoriniGameStateManager:
    """Driver class for a command-line REPL interface to the Santorini game"""

    def __init__(self):
        self.game = Game()
        self.state = PickPieceState()

    def start(self):
        """Start the game with the provided board state."""
        while True:
            self.state.handle_input(self.game)
            self.state.update(self.game)
        
if __name__ == "__main__":
    try:
        manager = SantoriniGameStateManager()  # Create an instance of SantoriniGameStateManager
        manager.start()  # Call the start method on the instance
    except Exception as e:
        print("Sorry! Something unexpected happened.")
        sys.exit(0)