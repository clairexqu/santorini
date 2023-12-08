from turn import Turn
from coordinate import Coordinate

DIRECTION_TRANSFORMATION = {
    "n": Coordinate(-1, 0),
    "ne": Coordinate(-1, 1),
    "e": Coordinate(0, 1),
    "se": Coordinate(1, 1),
    "s": Coordinate(1, 0),
    "sw": Coordinate(1, -1),
    "w": Coordinate(0, -1),
    "nw": Coordinate(-1, -1),
}


class Player:
    def __init__(self, color, workers):
        """
        Define a general player of the game, from which the actual players
        will inherit (template).
        """
        self._color = color
        self._workers = workers

    def build_turn(self, turn, board):
        pass

    def __str__(self):
        """Return the current board state."""
        player_str = ""
        player_str += f"{self._color} ("
        for worker in self._workers:
            player_str += f"{str(worker)}"
        player_str += ")"

        return player_str


class HumanPlayer(Player):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_worker(self):
        return input("Select a worker to move\n").upper()

    def get_placement(self):
        return input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n").lower()

    def get_build(self):
        return input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n").lower()

    def build_turn(self, turn, board):
        turn.worker = self.get_worker()
        turn.placement_direction = self.get_placement()
        
        turn.build_direction = self.get_build()


class AIPlayer(Player):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self):
        pass

    def build():
        pass

    # IMPLEMENT random build

    def build_turn(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AIHeuristic(AIPlayer):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # IMPLEMENT

    def build(self):
        pass

    def build_turn(self):
        pass


class AIRandom(AIPlayer):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # IMPLEMENT

    def build(self):
        pass

    def build_turn(self):
        pass
