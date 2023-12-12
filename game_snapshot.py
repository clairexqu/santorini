from copy import deepcopy

class CommandSnapshot:
    """Class representing a deep copied turn command which contains the board after a certain turn is executed."""

    def __init__(self, do_turn_command):
        self._do_turn_command = deepcopy(do_turn_command)

    def get_board(self):
        """Returns a turn command."""
        return self._do_turn_command.board

# FINAL DRAFT 