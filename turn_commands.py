import abc

from turn import Turn

class Command(abc.ABC):
    """Abstract base class for commands."""

    @abc.abstractmethod
    def execute(self):
        """Execute the command."""
        pass

class TurnBuilderCommand(Command):
    """Command class for building a move object for a specific player."""

    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.turn = Turn()

    def execute(self):
        # Build the turn object for the player
        self.player.build_turn(self.turn, self.board)

    def get_turn(self):
        return self.turn

# class DoTurnCommand(Command):
#     """Concrete command class for executing a move operation."""

#     def execute(self):
#         self.board.move(self.move)

# class Board:
#     """Sample board class."""

#     def move(self, move):
#         # Implement the logic for moving on the board
#         print(f"Moving on the board with move: {move}")

# # Usage example
# board = Board()

