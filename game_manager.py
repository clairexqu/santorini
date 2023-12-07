import sys
import abc
from game import Game 

class GameManagerState(metaclass=abc.ABCMeta):
    """Base class for game states."""
    @abc.abstractmethod
    def handle_state(self):
        raise NotImplementedError()

# class PickPieceState(GameManagerState):
#     """State representing the movement phase."""

#     def handle_state(self):
#         worker = input("Select a worker to move: ")
#         #manager.game....

#     def update(self):
#         if game.is_game_over():
#             game.state(GameOverState())


# class PlacementState(GameManagerState):
#     """State representing the worker placement phase."""

#     def handle_state(self):
#         position = input("Select a position to place the worker (row column): ")
#         #game.place_worker(worker, row, col)

#     def update(self, game):
#         if game.is_placement_complete():
#             game.state(BuildingState())


# class BuildingState(GameManagerState):
#     """State representing the building phase."""

#     def handle_state(self):
#         position = input("Select a position to build (row column): ")
#         game.build_level(row, col)

#     def update(self, game):
#         if game.is_building_complete():
#             game.state(MovementState())


class SetUpState(GameManagerState):
    """State representing ..."""

    def handle_state(self):
        manager.game = Game()
        manager.state(PlayGameState)

class PlayGameState(GameManagerState):
    """State representing ..."""

    def handle_state(self):
        pass
        if manager.game.is_game_over(): #maybe have it as a method instead of actual boolean
             manager.state(GameOverState())

class GameOverState(GameManagerState):
    """State representing the game over phase."""

    def handle_state(self):
        choice = input("The game is over. Would you like to play another game? (yes/no): ")
        if choice.lower() == "yes":
            manager.state(SetUpState())
        else:
            sys.exit(0)

class GameManager:
    """Driver class for a command-line REPL interface to the Santorini game"""

    def __init__(self):
        self.game = None
        self.state = SetUpState()

    def start(self):
        """Start the game with the provided board state."""
        while True:
            self.state.handle_state()
            self.state.update()
        
if __name__ == "__main__":
    try:
        manager = GameManager()  # Create an instance of SantoriniGameStateManager
        manager.start()  # Call the start method on the instance
    except Exception as e:
        print("Sorry! Something unexpected happened.")
        sys.exit(0)