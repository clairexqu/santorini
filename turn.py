from coordinate import Coordinate


class Turn:
    def __init__(self):
        self.worker = None
        self.placement_direction = None
        self.build_direction = None
        self.placement_transformation_coordinate = None 
        self.build_transformation_coordinate = None  

    def __str__(self):
        """Return the current board state."""
        turn_str = "" f"{self.worker}, {self.placement_direction}, {self.build_direction}"

        return turn_str
