import sys

from game import Game

class SantoriniCLI:
    """Driver class for a command-line REPL interface to the Santorini game"""

    def __init__(self):
        self._game = Game()

        self._choices = {
            "1": self._start_game,
            "2": self._quit,
        }

    def _display_menu(self):
        print("""--------------------------------
Enter command
1: Start game
2: Quit""")

    def run(self):
        """Display the menu and respond to choices."""

        while True:
            self._display_menu()
            choice = input(">")
            action = self._choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def _start_game(self):
        print("Starting Santorini game...")
        self._game.start()

    def _quit(self):
        sys.exit(0)


if __name__ == "__main__":
    try:
        SantoriniCLI().run()
    except Exception as e:
        print("Sorry! Something unexpected happened. Check the logs or contact the developer for assistance.")
        sys.exit(0)