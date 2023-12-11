from copy import deepcopy

class CommandSnapshot:
    """Class representing a snapshot of the board at a certain turn."""
    def __init__(self, do_turn_command):
        self._do_turn_command = deepcopy(do_turn_command) 

    def get_board(self):
        """Returns a snapshot of the board when called."""
        return self._do_turn_command.board