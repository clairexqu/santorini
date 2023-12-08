from coordinate import Coordinate


class Turn:
    def __init__(self, worker=None, placement_direction=None, build_direction=None):
        self.worker = worker
        self.placement_direction = placement_direction
        self.build_direction = build_direction

    def __str__(self):
        """Return the current board state."""
        turn_str = "" f"{self.worker}, {self.placement_direction}, {self.build_direction}"

        return turn_str
