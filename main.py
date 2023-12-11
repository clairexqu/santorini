
from abc import ABCMeta, abstractmethod
from sys import exit, argv
from game import Game 

class GameManagerState(metaclass=ABCMeta):
    """Base class for game states."""
    @abstractmethod
    def handle_state(self):
        raise NotImplementedError()

class SetUpState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager):
        #print("1. Game set up\n")

        #print(str(manager.settings))

        player1_type = "human"
        player2_type = "human"
        undo_enabled = False
        score_display_enabled = True

                # Exclude the script name itself
        length_settings = len(manager.settings)
        # Override default values with command line settings
        if length_settings >= 1:
            player1_type = manager.settings[0]
        if length_settings >= 2:
            player2_type = manager.settings[1]
        if length_settings >= 3 and manager.settings[2] == "on":
            undo_enabled = True
        if length_settings >= 4 and manager.settings[3] == "on":
            score_display_enabled = True
        
        #print(player1_type) 
        #print(player2_type) 
        #print(str(undo_enabled)) 
        #print(str(score_display_enabled)) 

        manager.game = Game(player1_type, player2_type, undo_enabled, score_display_enabled)
        manager.state = TurnState()

class TurnState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager): #executes a turn 
        #print("2. Play game state\n")
        #manager.game.print_board()
        print(str(manager.game))
        
        win_summary = manager.game.is_game_over()

        if win_summary: #maybe have it as a method instead of actual boolean
            # print("SOMEONE HAS WON\n")
            print(win_summary)
            manager.state = GameOverState()
        else:
            # print("GAME EXECUTE TURN\n")
             turn_summary = manager.game.execute_turn()
             if turn_summary:
                print(turn_summary)
             #self.undo_redo_next()
                
    def undo_redo_next():
        undo_redo_next = input("undo, redo, or next\n").lower()
        if undo_redo_next == "undo":
            manager.state = UndoState()
        elif undo_redo_next == "redo":
            manager.state = RedoState()
        # if next then GameManager stays as Turn State
        
class UndoState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager): 

        manager.state = TurnState()

class RedoState(GameManagerState):
    """State representing ..."""

    def handle_state(self, manager): 

        manager.state = TurnState()    

class GameOverState(GameManagerState):
    """State representing the game over phase."""

    def handle_state(self, manager):
        choice = input("Play again?\n")
        if choice.lower() == "yes":
            manager.state = SetUpState()
        else:
            exit(0)

class GameManager:
    """Driver class for a command-line REPL interface to the Santorini game"""

    def __init__(self, settings):
        self.game = None
        self.settings = settings
        self.state = SetUpState()
        

    def start(self):
        """Start the game with the provided board state."""

        while True:
            self.state.handle_state(self)
            #self.state.update()


if __name__ == "__main__":
    settings = argv[1:]  # Exclude the script name itself
    manager = GameManager(settings)
    manager.start()

# if __name__ == "__main__":
#     manager = GameManager()  # Create an instance of SantoriniGameStateManager
#     manager.start()  # Call the start method on the instance
#     # try:
#     #     manager = GameManager()  # Create an instance of SantoriniGameStateManager
#     #     manager.start()  # Call the start method on the instance
#     # except Exception as e:
#     #     print("Sorry! Something unexpected happened.")
#     #     sys.exit(0)