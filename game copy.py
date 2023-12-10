from board import Board
from player import HumanPlayer, AIRandomPlayer
from turn_commands import TurnBuilderCommand, DoTurnCommand
from game_snapshot import CommandSnapshot  # GameSnapshot
from sys import exit  # delete


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
        self._command_history = []
        self._command_history_index = 0
        self.create_snapshot(DoTurnCommand(self._board))

    def create_player():
        pass

    def execute_turn(self):
        # self._print_turn_info()

        undo_redo_next = input("undo, redo, or next\n").lower()

        if undo_redo_next == "undo":
            self.execute_undo()
            return None

        self._command_history_index += 1

        current_player = self._current_player()

        turn_builder_command = TurnBuilderCommand(self._board, current_player)
        turn_builder_command.execute()

        do_turn_command = DoTurnCommand(self._board, turn_builder_command.turn)
        do_turn_command.execute()

        # print(len(self._command_history))
        # print(self._turn_number)
        # self._command_history = self._command_history[:self._turn_number - 1]

        print("TURN # " + str(self._turn_number))
        print("COMMAND INDEX: " + str(self._command_history_index))

        # if self._command_history_index != self._turn_number:
        # new_command_history = []
        # for number in self._command_history_index:
        # new_command_history = []
        #    new_command_history.append(self._command_history[number - 1])

        # new_command_history = self._command_history[0:self._command_history_index]
        # snapshot = CommandSnapshot(do_turn_command)
        # new_command_history.append(snapshot)
        # self._command_history = new_command_history

        if len(self._command_history) != self._turn_number:
            print(len(self._command_history))
            print(str(self._turn_number))
            num_pops = (len(self._command_history) - self._turn_number) + 1
            for _ in range(num_pops):
                print("here")
                self._command_history.pop()

        # self._command_history.append(snapshot)

        # self._command_history = self._command_history[0:self._command_history_index - 1]

        # if len(self._command_history) != self._turn_number:
        #     #self._command_history = self._command_history[0:(int(self._turn_number))]
        #     new_command_history = []
        #     for index in range(0, self._turn_number):
        #         new_command_history.append(self._command_history[index])

        #     self._command_history = new_command_history

        #     print("COMMAND LEN AFTER EDIT: " + str(len(self._command_history)))

        self._turn_number = self._turn_number + 1
        turn_summary = str(do_turn_command.turn)
        self.create_snapshot(do_turn_command)

        index = 0
        print("############")
        for command in self._command_history:
            print(str(index) + ":\n" + str(command.get_board()) + "\n")
            index += 1

        print("############")

        return turn_summary

    def create_snapshot(self, do_turn_command):
        # Create a GameSnapshot and store it in the history
        snapshot = CommandSnapshot(do_turn_command)
        self._command_history.append(snapshot)

    def execute_undo(self):
        # Restore the previous game state from the history
        # print(str(len(self._command_history)))
        # print(str(self._turn_number))

        # # if going back to to before any turn was made n
        # if self._turn_number - 1 == 0:
        #     self._board = Board()
        #     return None
        #     # print(str(self))
        #     # exit(0)

        print("\n\n")
        if self._turn_number == 1:
            command_snapshot = self._command_history[self._turn_number - 1]
            return None
        else:
            self._turn_number -= 1
            #self._command_history_index -= 1
            command_snapshot = self._command_history[self._turn_number - 1]
            #command_snapshot = self._command_history[self._turn_number - 1]
            # previous_command_snapshot = self._command_history[self._turn_number - 1]

        index = 0
        print("############")
        for command in self._command_history:
            print(str(index) + ":\n" + str(command.get_board()) + "\n")
            index += 1

        print("############")

        self._board = command_snapshot.get_board()
        # return str(previous_command_snapshot.get_turn())
        # print(command_snapshot.get_turn())
        # print(str(self))
        # exit(0)
        # turn = command_snapshot.get_turn()
        # if turn:
        #    return str(command_snapshot.get_turn())

    def execute_redo(self):
        self._turn_number += 1

        command_snapshot = self._command_history[self._turn_number]
        self._board = command_snapshot.get_board()
        # print(str(self._board))
        # exit(0)
        return str(command_snapshot.get_turn())

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
