from board import Board
from player import HumanPlayer, AIRandomPlayer, AIHeuristicPlayer
from turn_commands import TurnBuilderCommand, DoTurnCommand
from game_snapshot import CommandSnapshot


class Game:
    """Class representing the Santorini game. Has a board, the player types, settings such as if undo/redo is enabled
    and if score display is enabled, the current turn number, and two lists which hold command snapshots and act as the undo stack and redo stack
    """

    def __init__(
        self, player1_type, player2_type, undo_redo_enabled, score_display_enabled
    ):
        self._board = Board()

        self._enable_undo_redo = undo_redo_enabled
        self._score_display_enabled = score_display_enabled

        # Note that player 1 must be second in the list in order for them to go first
        self._players = [
            self._create_player(player2_type, "blue", ["Y", "Z"]),
            self._create_player(player1_type, "white", ["A", "B"]),
        ]
        self._turn_number = 1
        self._command_history_undo = []
        self._command_history_redo = []

    def _create_player(self, type, color, workers):
        if type == "human":
            return HumanPlayer(color, workers)
        elif type == "heuristic":
            return AIHeuristicPlayer(color, workers)

        return AIRandomPlayer(color, workers)

    def execute_turn(self):
        """Executes a turn by through the turn builder command and the do turn command.
        Returns a turn summary (None if redo or undoing a turn)"""

        if self._enable_undo_redo:
            undo_redo_next = input("undo, redo, or next\n").lower()

            if undo_redo_next == "undo":
                self._execute_undo()
                return None

            if undo_redo_next == "redo":
                self._execute_redo()
                return None

            # If reached then user typed next. The redo command list is emptied because you cannot Next and then Redo
            self._command_history_redo = []

        current_player = self._current_player()

        turn_builder_command = TurnBuilderCommand(self._board, current_player)
        turn_builder_command.execute()

        do_turn_command = DoTurnCommand(self._board, turn_builder_command.turn)
        do_turn_command.execute()

        self._turn_number = self._turn_number + 1

        turn_summary = str(do_turn_command.turn)

        # If score display is enabled then info about the move score is added to the turn summary
        if self._score_display_enabled:
            turn_summary += f" {str(do_turn_command.turn.move_score)}"

        self._create_snapshot(do_turn_command)

        return turn_summary

    def _create_snapshot(self, do_turn_command):
        # Create a GameSnapshot and pushes it to undo history stack
        snapshot = CommandSnapshot(do_turn_command)
        self._command_history_undo.append(snapshot)

    def _execute_undo(self):
        length = len(self._command_history_undo)

        # This handles the case where if the user wants to undo back to the state where a turn hasn't been made (from turn 2 to turn 1)
        if length == 1:
            self._turn_number -= 1
            self._command_history_redo.append(self._command_history_undo.pop())
            self._board = Board()

        if length > 1:
            self._turn_number -= 1
            # Pops last command in the undo stack and pushes it to the redo stack
            self._command_history_redo.append(self._command_history_undo.pop())
            # Sets the board to be the board of the last command snapshot in the undo stack
            command_snapshot = self._command_history_undo[-1]
            self._board = command_snapshot.get_board()

    def _execute_redo(self):
        length = len(self._command_history_redo)

        if length > 0:
            self._turn_number += 1

            # Sets the board to be the board of the last command snapshot in the redo stack
            command_snapshot = self._command_history_redo[-1]
            self._board = command_snapshot.get_board()
            # Pops last command in the redo stack and pushes it to the undo stack
            self._command_history_undo.append(self._command_history_redo.pop(-1))

    def _current_player(self):
        return self._players[self._turn_number % 2]

    def __str__(self):
        """Returns the game summary which is a string of the board and information about the current turn and current player."""

        game_str = f"{str(self._board)}\nTurn: {str(self._turn_number)}, {str(self._current_player())}"

        if self._score_display_enabled:
            turn = self._current_player().build_fake_turn(self._board)
            game_str += f", {str(turn.move_score)}"

        return game_str

    def is_game_over(self):
        """Checks if a player has won or not. Returns a string that dictates the winner or None if no one has won."""
        current_player = self._current_player()
        current_player.build_valid_placements(self._board)

        # Checks if a player can't make a turn. If they can't then the other player wins
        if len(current_player._valid_placements) == 0:
            next_player = self._players[(self._turn_number + 1) % 2]
            return f"{next_player._color} has won"
        
        # Checks if a player has won via one of their workers being in a cell of height 3 
        winner_worker = self._board.winner_worker
        if winner_worker:
            for player in self._players:
                if winner_worker in player._own_workers:
                    return f"{player._color} has won"
        return None
