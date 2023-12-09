from board import Board
from player import HumanPlayer, AIRandomPlayer
from turn_commands import TurnBuilderCommand, DoTurnCommand
from game_snapshot import GameSnapshot


class Game:
    """Class representing the Santorini game"""

    def __init__(self):
        self._board = Board()
        self.enable_undo_redo = False
        self.enable_score_display = False

        self.players = [
            AIRandomPlayer("blue", ["Y", "Z"]),
            AIRandomPlayer("white", ["A", "B"]),
        ]
        self._turn_number = 1
        self._history = []

    def create_player():
        pass

    def execute_turn(self):
        # self._print_turn_info()

        # Build the move
        #turn_summary = ""

        # undo_redo_next = input("undo, redo, or next\n").lower()
        # if undo_redo_next == "undo":
        #     turn_summary = self.execute_undo()
        #     return turn_summary
        # elif undo_redo_next == "redo":
        #     turn_summary = self.execute_redo()
        #     return turn_summary

        current_player = self._current_player()

        turn_builder_command = TurnBuilderCommand(self._board, current_player)
        turn_builder_command.execute()
        turn = turn_builder_command.get_turn()

        do_turn = DoTurnCommand(self._board, turn)
        do_turn.execute()

        self._turn_number = self._turn_number + 1

        turn_summary = str(turn)
        self.create_snapshot(turn_summary)

        return turn_summary
    
    def execute_undo_redo_next(self):
        pass
       
    def create_snapshot(self, turn_summary):
        # Create a GameSnapshot and store it in the history
        snapshot = GameSnapshot(self._board, turn_summary)
        self._history.append(snapshot)
    
    def execute_undo(self):
        if len(self._history) > 0:
            # Restore the previous game state from the history
            self._turn_number -= - 1
            game_snapshot = self._history[self._turn_number]
            self._board = game_snapshot.board_state
            return game_snapshot.turn_summary 
            #self._turn_number = snapshot.next_turn_number - 1

    def execute_redo(self):
        if len(self._history) < len(self._history):
            # Restore the next game state from the history
            snapshot = self._history[self._turn_number]
            self._board = snapshot.board_state
            self._turn_number = snapshot.next_turn_number


    def _current_player(self):
        return self.players[self._turn_number % 2]

    def __str__(self):
        # USE THIS EVENTUALLY
        game_str = ""
        game_str += f"{str(self._board)}\nTurn: {str(self._turn_number)}, {str(self._current_player())}"
        return game_str

    # def _print_turn_info(self):
    #     print("Turn: " + str(self.turn) + " player: " + str(self.turn % 2) + "\n")
    #     pass

    def print_board(self):
        print(str(self._board))

    def is_game_over(self):
        current_player = self._current_player()
        current_player._build_valid_placements(self._board)

        if len(current_player._valid_placements) == 0:
            next_player = self.players[(self._turn_number + 1) % 2]
            return f"{next_player._color} has won"

        winner_worker = self._board.winner_worker
        if winner_worker:
            for player in self.players:
                if winner_worker in player._own_workers:
                    return f"{player._color} has won"
        return None