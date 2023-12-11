from turn import Turn
from coordinate import Coordinate
from random import choice


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
    """Define a general player of the game, from which the actual players will inherit (template), 
    with a color, workers, and a list of valid placements and builds."""
    def __init__(self, color, workers):
        self._color = color
        self._own_workers = workers
        self._valid_placements = [] # This is a list of turns 
        self._valid_builds = [] # This is a list of directions

    def build_valid_placements(self, board):
        """Creates a list of all the valid worker and placement combinations for a player.""" 
        self._valid_placements = []
        # Loops through a player's own workers
        for worker in self._own_workers:
            current_worker_coordinate = board.workers[worker]

            # Loops through all the possible directions for a worker and gets the coordinates
            for placement_direction, placement_coordinate in DIRECTION_TRANSFORMATION.items():
                turn = Turn(worker, placement_direction, placement_coordinate)
                turn.calc_placement_coordinate(current_worker_coordinate)

                # If the coordinate is avlid
                if self._valid_placement(current_worker_coordinate, turn.placement_coordinate, board):
                    # Calculate height score, center score, distance score
                    self._calc_score(board, turn)
                    # Add it to the list of valid placements for a player
                    self._valid_placements.append(turn)                 

    def _calc_score(self, board, turn):
        move_score = turn.move_score
        # Initializes a list of the player's workers, starting with the potential coordinate
        coordinates = [turn.placement_coordinate]

        # Get coordinate of the player's other worker and add it to the list
        for worker in self._own_workers:
            if worker != turn.worker:
                other_worker_coordinate = board.workers[worker]
                coordinates.append(other_worker_coordinate)

        # Calculates the height and center score for each worker in a player's potential placement
        for coordinate in coordinates:
            move_score.height_score += self._calculate_height_score(board, coordinate, turn.move_score)
            move_score.center_score += self._calculate_center_score(coordinate)

        # Get a list of the other player's worker's coordinates
        enemy_coordinates = []
        for worker in board.workers:
            if worker not in self._own_workers:
                enemy_coordinates.append(board.workers[worker])

        distance_before_eight = 0
        # Loops through opponent's coordinates to calculate the distance score
        for enemy_coordinate in enemy_coordinates:
            distance_before_eight += self._calculate_distance_score(enemy_coordinate, coordinates)
        move_score.distance_score = 8 - distance_before_eight

        move_score.calc_total_score()
                    
    def _valid_placement(self, old_coordinate, new_coordinate, board):
        # Checks if placement is in bounds 
        new_row = new_coordinate.row
        new_column = new_coordinate.column
        if (new_row < 0 or new_row > 4) or (new_column < 0 or new_column > 4):
            return False
        # Checks if cell is occupied
        old_cell = board.get_cell(old_coordinate.row, old_coordinate.column)
        new_cell = board.get_cell(new_row, new_column) 
        if new_cell.worker_character != " ":
            return False
        # Checks cell height
        old_height = old_cell.height
        new_height = new_cell.height
        if new_height == 4 or new_height - old_height > 1:
            return False
        return True
    
    def _calculate_height_score(self, board, coordinate, move_score):
        # Height_score is the sum of the heights of the buildings a player's workers stand on
        # Get height of worker in hypothetical turn
        row = coordinate.row
        column = coordinate.column
        height_score = board.get_cell(row, column).height
        # Extra weight if the turn can get the player a win
        if height_score == 3:
            move_score.total_score += 100

        return height_score        

    def _calculate_center_score(self, coordinate):
        # Value the center space as 2, the ring around the center as 1, the edge spaces as 0
        # Add these values for each of a player's workers to get the center_score
        row = coordinate.row 
        column = coordinate.column 

        # If the worker is in the center square
        if row == 2 and column == 2:
            return 2
        # If the worker is in the middle ring
        elif (row == 1 or row == 2 or row == 3) and (column == 1 or column == 2 or column == 3):
            return 1
        # If the worker is in the outer ring  
        else:
            return 0

    def _calculate_distance_score(self, enemy_coordinate, own_coordinates):
        # Enemy coordinate is a single coordinate, own_coordinate is a list
        
        # Distance_score is the sum of the minimum distance to the opponent's workers
        distance_scores = []

        # Calculates distance from both workers to an enemy coordinate
        for own_coordinate in own_coordinates:
            distance = self._distance_between(own_coordinate, enemy_coordinate)
            distance_scores.append(distance)

        # Return the minimum distance for that enemy coordinate
        return min(distance_scores)

    def _distance_between(self, own_coordinate, enemy_coordinate):
        dist1 = abs(own_coordinate.row - enemy_coordinate.row)
        dist2 = abs(own_coordinate.column - enemy_coordinate.column)
        # Returns the chess distance between two coordinates
        return max(dist1, dist2)
    
    def _build_valid_builds(self, turn, board):
        self._valid_builds = []
        # Loops through all the possible build directions for a placement
        for placement_direction, build_coordinate in DIRECTION_TRANSFORMATION.items():
            potential_build_coordinate = turn.placement_coordinate + build_coordinate
            # If the build is possible, add it to the list
            if self._valid_build(turn.worker, potential_build_coordinate, board):
                self._valid_builds.append(placement_direction)

    def _valid_build(self, worker, build_coordinate, board):    
        # Check if build is out of bounds
        build_row = build_coordinate.row
        build_column = build_coordinate.column
        if (build_row < 0 or build_row > 4) or (build_column < 0 or build_column > 4):
            return False
        # Check if cell has a dome
        cell = board.get_cell(build_coordinate.row, build_coordinate.column)
        if cell.height > 3:
            return False
        # Check if cell is occupied
        if cell.worker_character != worker and cell.worker_character != " ":
            return False      
        return True
    
    def build_fake_turn(self, board):
        """Builds a dummy turn to print the score of a move a player has already taken."""
        coordinate = board.workers[self._own_workers[0]]
        turn = Turn(self._own_workers[0])
        turn.placement_coordinate = coordinate
        self._calc_score(board, turn)
        return turn 

    def build_turn(self):
        """Abstract method that builds a turn for a certain player."""
        pass

    def __str__(self):
        """Returns the player summary to prompt for a turn."""
        player_str = ""
        player_str += f"{self._color} ("
        for worker in self._own_workers:
            player_str += f"{str(worker)}"
        player_str += ")"
        return player_str

class HumanPlayer(Player):
    """Class representing a human player of the Santorini game."""
    def _worker_has_turn(self, potential_worker):
        for turn in self._valid_placements:
            if turn.worker == potential_worker:
                return True
        return False

    def _get_worker(self, workers_dict):
        # Prompts human user for a worker until it is correct
        while True:
            selected_worker = input("Select a worker to move\n").upper()
            if selected_worker not in workers_dict:
                print("Not a valid worker")
                continue
            elif selected_worker not in self._own_workers:
                print("That is not your worker")
                continue
            elif not self._worker_has_turn(selected_worker):
                print("That worker cannot move")
                continue
            return selected_worker

    def _get_placement(self, worker):
        # Prompts human user for a placement until it is correct
        while True:
            selected_placement = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n").lower()
            if selected_placement not in DIRECTION_TRANSFORMATION:
                print("Not a valid direction")
                continue
            turn = self._get_valid_turn(worker, selected_placement)
            if not turn:
                print(f"Cannot move {selected_placement}")
                continue
            return turn

    def _get_build(self):
        # Prompts human user for a build until it is correct
        while True:
            selected_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n").lower()
            if selected_build not in DIRECTION_TRANSFORMATION:
                print("Not a valid direction")
                continue
            if selected_build not in self._valid_builds:
                print(f"Cannot build {selected_build}")
                continue
            return selected_build

    def _get_valid_turn(self, worker, potential_placement):
        # Get the specified turn from the list of valid placements
        for turn in self._valid_placements:
            if turn.worker == worker and turn.placement_direction == potential_placement:
                return turn
        return None
        
    def build_turn(self, board):
        """Method that builds a turn for a human player."""
        # Builds the list of valid placements, and the valid worker and placement from the user
        self.build_valid_placements(board)
        valid_worker = self._get_worker(board.workers)
        turn = self._get_placement(valid_worker)

        # Builds the list of valid builds, and the build the user wants
        self._build_valid_builds(turn, board)
        build_direction = self._get_build()
        turn.build_direction = build_direction
        turn.build_transformation_coordinate = DIRECTION_TRANSFORMATION[build_direction]
        turn.calc_build_coordinate()

        # Return the turn with all the needed fields
        return turn

class AIPlayer(Player):
    """Class representing any AI player of the Santorini game."""
    def _get_player_and_placement(self):
        # Abstract implementation lets AI classes override
        pass

    def _get_build(self):
        # Same method for all AI players
        return choice(self._valid_builds)

    def build_turn(self, board):
        """Builds a turn for an AI player."""
        self.build_valid_placements(board)
        turn = self._get_player_and_placement()

        self._build_valid_builds(turn, board)
        build_direction = self._get_build()
        turn.build_direction = build_direction
        turn.build_transformation_coordinate = DIRECTION_TRANSFORMATION[build_direction]
        turn.calc_build_coordinate()

        # Returns turn with all the needed fields
        return turn        

class AIRandomPlayer(AIPlayer):
    """Class representing a random AI player of the Santorini game."""
    def _get_player_and_placement(self):
        # Random choice of all the valid players and placements
        return choice(self._valid_placements)

class AIHeuristicPlayer(AIPlayer):
    """Class representing a heuristic AI player of the Santorini game."""
    def _get_player_and_placement(self):
        # Player and placement combination with the highest total move score
        return max(self._valid_placements, key=lambda placement: placement.move_score.total_score)