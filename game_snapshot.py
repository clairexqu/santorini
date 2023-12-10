from copy import deepcopy

class CommandSnapshot:
    def __init__(self, do_turn_command):
        self._do_turn_command = deepcopy(do_turn_command)  # Deep copy of the board
        #self.next_turn_number = next_turn_number
        #self.turn_summary = turn_summary
    
    def get_board(self):
        return self._do_turn_command.board
    
    def get_turn(self):
        return self._do_turn_command.turn

# class GameSnapshot:
#     def __init__(self, board, turn_summary):
#         self.board_state = deepcopy(board)  # Deep copy of the board
#         #self.next_turn_number = next_turn_number
#         self.turn_summary = turn_summary

# class GameCommandHistory:
#     def __init__(self):
#         self.command_history = []

#     def create_snapshot(self, command):
#     #    Create a GameSnapshot and store it in the history
#          snapshot = CommandSnapshot(self._board)
#          self.command_history.append(snapshot)
        
