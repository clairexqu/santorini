from coordinate import Coordinate

class Turn:
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
        self.placement_coordinate = self.placement_transformation_coordinate + old_coordinate
    
    def calc_build_coordinate(self):
        self.build_coordinate = self.build_transformation_coordinate + self.placement_coordinate

    def __str__(self):
        """Return the current board state."""
        #turn_str = "" f"Worker: {self.worker}\nPlacement Direction: {self.placement_direction}\nPlacement Transformation Coord: {self.placement_transformation_coordinate}\nNew Placement Coordinate: {self.placement_coordinate}\nBuild Direction: {self.build_direction}\nBuild Transformation Coord: {self.build_transformation_coordinate}\nNew Build Coord: {self.build_coordinate}"
        turn_str = f"{self.worker}, {self.placement_direction}, {self.build_direction}"

        return turn_str

class MoveScore:
    def __init__(self):
        self.height_score = 0
        self.can_win = False
        self.center_score = 0
        self.distance_score = 0
        self.total_score = 0 
        
    def calc_total_score(self):
        if self.can_win:
            self.total_score = 100 * self.height_score + 2 * self.center_score + 1 * self.distance_score
        self.total_score = 3 * self.height_score + 2 * self.center_score + 1 * self.distance_score

    def __str__(self):
        """Return the current board state."""
        #turn_str = "" f"Worker: {self.worker}\nPlacement Direction: {self.placement_direction}\nPlacement Transformation Coord: {self.placement_transformation_coordinate}\nNew Placement Coordinate: {self.placement_coordinate}\nBuild Direction: {self.build_direction}\nBuild Transformation Coord: {self.build_transformation_coordinate}\nNew Build Coord: {self.build_coordinate}"
        move_score_str = f"({self.height_score}, {self.center_score}, {self.distance_score})"

        return move_score_str