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
        # print("1. Game set up\n")
        manager.game = Game()
        manager.state = PrintGameState()


class PrintGameState(GameManagerState):
    def handle_state(self, manager):  
     
        print(str(manager.game))

        win_summary = manager.game.is_game_over()

        if win_summary:  # maybe have it as a method instead of actual boolean
            # print("SOMEONE HAS WON\n")
            print(win_summary)
            manager.state = GameOverState()
        else:
            # print("GAME EXECUTE TURN\n")
            manager.state = TurnState()
            #manager.state = getUndoRedoNextState()

class getUndoRedoNextState(GameManagerState):
    def handle_state(self, manager):
        undo_redo_next = input("undo, redo, or next\n").lower()
        if undo_redo_next == "undo":
            manager.state = UndoState()
        elif undo_redo_next == "redo":
            manager.state = RedoState()
        else: 
            manager.state = NextState()

class UndoState(GameManagerState):
    def handle_state(self, manager):
        manager.state = TurnState()

class RedoState(GameManagerState):

    def handle_state(self, manager):
        manager.state = TurnState()

class NextState(GameManagerState):
    def handle_state(self, manager):
        manager.state = TurnState()

class TurnState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager):  # executes a turn
        turn_summary = manager.game.execute_turn()
        print(turn_summary)
        manager.state = SetUpState()

class GameOverState(GameManagerState):
    """State representing the game over phase."""

    def handle_state(self, manager):
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
            # self.state.update()


if __name__ == "__main__":
    manager = GameManager()  # Create an instance of SantoriniGameStateManager
    manager.start()  # Call the start method on the instance
    # try:
    #     manager = GameManager()  # Create an instance of SantoriniGameStateManager
    #     manager.start()  # Call the start method on the instance
    # except Exception as e:
    #     print("Sorry! Something unexpected happened.")
    #     sys.exit(0)
