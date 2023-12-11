class Turn:
    """Class representing a turn in the Santorini game, with its respective worker, 
    placement with its coordinate, possible transformation and move score, and build
    with its coordinate."""
    def __init__(self, worker = None, placement_direction = None, placement_transformation_coordinate = None, build_direction = None, build_transformation_coordinate = None):
        self.worker = worker
        self.placement_direction = placement_direction
        self.placement_transformation_coordinate = placement_transformation_coordinate
        self.placement_coordinate = None 
        self.move_score = MoveScore()

        self.build_direction = build_direction 
        self.build_transformation_coordinate = build_transformation_coordinate
        self.build_coordinate = None 

    def calc_placement_coordinate(self, old_coordinate):
        """Calculates the final placement coordinate of a worker."""
        self.placement_coordinate = self.placement_transformation_coordinate + old_coordinate
    
    def calc_build_coordinate(self):
        """Calculates the final coordinate of a build."""
        self.build_coordinate = self.build_transformation_coordinate + self.placement_coordinate

    def __str__(self):
        """Returns the turn summary."""
        turn_str = f"{self.worker},{self.placement_direction},{self.build_direction}"
        return turn_str

class MoveScore:
    """Class representing a placement's move score, made up of a height, center, and distance score."""
    def __init__(self):
        self.height_score = 0
        self.center_score = 0
        self.distance_score = 0
        self.total_score = 0 
        
    def calc_total_score(self):
        """Uses a weighted formula to calculate the total score for a placement depending on the three parts."""
        self.total_score += 3 * self.height_score + 2 * self.center_score + 1 * self.distance_score

    def __str__(self):
        """Returns the move score summary."""
        move_score_str = f"({self.height_score}, {self.center_score}, {self.distance_score})"
        return move_score_str