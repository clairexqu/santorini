from abc import ABC, abstractmethod


class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass


class TurnBuilderCommand(Command):
    """Concrete command class for building a turn object for a specific player."""

    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.turn = None

    def execute(self):
        """Execute the build turn command."""
        # Build the turn object for the player
        self.turn = self.player.build_turn(self.board)


class DoTurnCommand(Command):
    """Concrete command class for executing a turn operation."""

    def __init__(self, board, turn=None):
        self.board = board
        self.turn = turn

    def execute(self):
        """Execute the turn."""
        # Executes the actual turn on the board
        self.board.execute_turn(self.turn)


# FINAL DRAFT
