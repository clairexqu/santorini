from abc import ABCMeta, abstractmethod
from sys import exit, argv
from game import Game


class GameManagerState(metaclass=ABCMeta):
    """Base class for game states."""

    @abstractmethod
    def handle_state(self):
        """Executes the current state and sets the new state for the game"""
        pass


class SetUpState(GameManagerState):
    """State representing the creation of a new game. Done at the beginning of a new game."""

    def handle_state(self, manager):
        """Executes the SetUpState. Creates a new game."""

        # Default values for all the settings
        player1_type = "human"
        player2_type = "human"
        undo_enabled = False
        score_display_enabled = False

        length_settings = len(manager.settings)
        # Overrides the default values with command line settings

        if length_settings >= 1:
            player1_type = manager.settings[0]
        if length_settings >= 2:
            player2_type = manager.settings[1]
        if length_settings >= 3 and manager.settings[2] == "on":
            undo_enabled = True
        if length_settings >= 4 and manager.settings[3] == "on":
            score_display_enabled = True

        manager.game = Game(
            player1_type, player2_type, undo_enabled, score_display_enabled
        )
        manager.state = TurnState()


class TurnState(GameManagerState):
    """State representing the turns of the game."""

    def handle_state(self, manager):
        """Executes the entirety of a turn including the prints"""

        print(str(manager.game))

        # gets a win summary (None if no one has won)
        win_summary = manager.game.is_game_over()

        # if there is a win summary print and go to game over state otherwise execute a full turn and print the turn summary
        if win_summary:
            print(win_summary)
            manager.state = GameOverState()
        else:
            turn_summary = manager.game.execute_turn()
            if turn_summary:
                print(turn_summary)


class GameOverState(GameManagerState):
    """State representing the game over phase."""

    def handle_state(self, manager):
        """Asks if the player wants to play again. If yes, a new game is set up. If not then exit the program."""
        choice = input("Play again?\n")
        if choice.lower() == "yes":
            manager.state = SetUpState()
        else:
            exit(0)


class GameManager:
    """Class acts as the manager of the Santorini game shifting between setting up the game, taking turns and ending the game"""

    def __init__(self, settings):
        self.game = None
        self.settings = settings
        self.state = SetUpState()

    def start(self):
        """Starts the game by handling the SetUpState."""

        while True:
            self.state.handle_state(self)


if __name__ == "__main__":
    settings = argv[1:]  # Exclude the script name itself
    manager = GameManager(settings)
    manager.start()
