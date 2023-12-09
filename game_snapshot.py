from copy import deepcopy

class GameSnapshot:
    def __init__(self, board, turn_summary):
        self.board_state = deepcopy(board)  # Deep copy of the board
        #self.next_turn_number = next_turn_number
        self.turn_summary = turn_summary

