from copy import deepcopy

class CommandSnapshot:
    def __init__(self, do_turn_command):
        self._do_turn_command = deepcopy(do_turn_command) 

    def get_board(self):
        return self._do_turn_command.board
    
    def get_turn(self):
        return self._do_turn_command.turn