import sys
import abc
from game import Game 

class GameManagerState(metaclass=abc.ABCMeta):
    """Base class for game states."""
    @abc.abstractmethod
    def handle_state(self):
        raise NotImplementedError()

class SetUpState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager):
        #print("1. Game set up\n")
        manager.game = Game()
        manager.state = PlayGameState()

class PlayGameState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager): #executes a turn 
        #print("2. Play game state\n")
        #manager.game.print_board()
        print(str(manager.game))
        manager.game.execute_turn()
        if manager.game.is_game_over(): #maybe have it as a method instead of actual boolean
             manager.state = GameOverState()

class GameOverState(GameManagerState):
    """State representing the game over phase."""

    def handle_state(self, manager):
        #print("game over\n")
        choice = input("Play again?\n")
        if choice.lower() == "yes":
            manager.state = SetUpState()
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
            self.state.handle_state(self)
            #self.state.update()
        
if __name__ == "__main__":
    manager = GameManager()  # Create an instance of SantoriniGameStateManager
    manager.start()  # Call the start method on the instance
    # try:
    #     manager = GameManager()  # Create an instance of SantoriniGameStateManager
    #     manager.start()  # Call the start method on the instance
    # except Exception as e:
    #     print("Sorry! Something unexpected happened.")
    #     sys.exit(0)