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
    def __init__(self, color, workers):
        """
        Define a general player of the game, from which the actual players
        will inherit (template).
        """
        self._color = color
        self._own_workers = workers
        self._valid_placements = [] # This is a list of turns 
        self._valid_builds = [] # This is a list of directions 

    def _build_valid_placements(self, board):     
        self._valid_placements = []
        
        for worker in self._own_workers:
            current_worker_coordinate = board.workers[worker]
            for placement_direction, placement_coordinate in DIRECTION_TRANSFORMATION.items():
                
                turn = Turn(worker, placement_direction, placement_coordinate)
                turn.calc_placement_coordinate(current_worker_coordinate)
                
                if self._valid_placement(current_worker_coordinate, turn.placement_coordinate, board):

                    # calculate height score, center score, distance score
                    turn.move_score.height_score = self._calculate_height_score(board, turn)
                    turn.move_score.center_score = self._calculate_center_score(board, turn)
                    turn.move_score.distance_score = self._calculate_distance_score(board, turn)
                    
                    self._valid_placements.append(turn) 
                    #print(str(turn))
                    #print(len(self._valid_placements))

    def _valid_placement(self, old_coordinate, new_coordinate, board):
        # checks if placement is in bounds 
        #print(str(board))
        #print(str(old_coordinate))
        new_row = new_coordinate.row
        new_column = new_coordinate.column
        if (new_row < 0 or new_row > 4) or (new_column < 0 or new_column > 4):
            return False
        #print(str(new_coordinate))
            # return False
        # checks if cell is occupied
        old_cell = board.get_cell(old_coordinate.row, old_coordinate.column)
        new_cell = board.get_cell(new_row, new_column) 
        if new_cell.worker_character != " ":
            return False
        # check cell height
# CHECK THAT THIS IS CORRECT LATER
        old_height = old_cell.height
        new_height = new_cell.height
        if new_height == 4 or new_height - old_height > 1:
            return False
        return True
    
    def _calculate_height_score(self, board, turn):
        # height_score is the sum of the heights of the buildings a player's workers stand on
        
        # get coordinate of player's other worker
        for worker in self._own_workers:
            if worker != turn.worker:
                other_worker_coordinate = board.workers[turn.worker]
                other_height = board.get_cell(other_worker_coordinate.row, other_worker_coordinate.column).height

        # get height of worker in hypothetical turn
        row = turn.placement_coordinate.row
        column = turn.placement_coordinate.column
        height = board.get_cell(row, column).height

        height_score = other_height + height
        return height_score

    def _calculate_center_score(self, board, turn):
        # value the center space as 2, the ring around the center as 1, the edge spaces as 0
        # add these values for each of a player's workers to get the center_score
        center_score = 0
        coordinates = [turn.placement_coordinate]

        # get coordinate of player's other worker
        for worker in self._own_workers:
            if worker != turn.worker:
                other_worker_coordinate = board.workers[turn.worker]
                coordinates.append(other_worker_coordinate)

        for coordinate in coordinates:
            # center square
            if coordinate.row == 2 and coordinate.column == 2:
                center_score += 2
            # outer ring
            elif (coordinate.row == 0 or coordinate.row == 4) and (coordinate.column == 0 or coordinate.column == 4):
                center_score += 0
            # middle ring
            else:
                center_score +=1
        return center_score

    def _calculate_distance_score(self, board, turn):
        # distance_score is the sum of the minimum distance to the opponent's workers
        # for blue, it would be min(distance from Z to A, distance from Y to A) + min(distance from Z to B, distance from Y to B)
        distance_score = 0

        return distance_score



    def _build_valid_builds(self, turn, board):
        self._valid_builds = []
        
        for placement_direction, build_coordinate in DIRECTION_TRANSFORMATION.items():
            potential_build_coordinate = turn.placement_coordinate + build_coordinate
            if self._valid_build(turn.worker, potential_build_coordinate, board):
                self._valid_builds.append(placement_direction)
                #print(placement_direction)

    def _valid_build(self, worker, build_coordinate, board):    
        # check if build is out of bounds
        build_row = build_coordinate.row
        build_column = build_coordinate.column
        if (build_row < 0 or build_row > 4) or (build_column < 0 or build_column > 4):
            return False
        # check if cell has a dome
        cell = board.get_cell(build_coordinate.row, build_coordinate.column)
# CHECK THIS IS CORRECT LATER
        if cell.height > 3:
            return False
        # check if cell is occupied
        if cell.worker_character != worker and cell.worker_character != " ":
            return False      
        return True

    def build_turn(self):
        pass

    def __str__(self):
        """Return the current board state."""
        player_str = ""
        player_str += f"{self._color} ("
        for worker in self._own_workers:
            player_str += f"{str(worker)}"
        player_str += ")"

        return player_str


class HumanPlayer(Player):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def worker_has_turn(self, potential_worker):
        for turn in self._valid_placements:
            if turn.worker == potential_worker:
                return True
        return False

    def get_worker(self, workers_dict):
        while True:
            selected_worker = input("Select a worker to move\n").upper()
            if selected_worker not in workers_dict:
                print("Not a valid worker")
                continue
            elif selected_worker not in self._own_workers:
                print("That is not your worker")
                continue
            elif not self.worker_has_turn(selected_worker):
                print("That worker cannot move")
                continue
            return selected_worker

    def get_placement(self, worker):
        while True:
            selected_placement = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n").lower()
            if selected_placement not in DIRECTION_TRANSFORMATION:
                print("Not a valid direction")
                continue
            turn = self.get_valid_turn(worker, selected_placement)
            if not turn:
                print(f"Cannot move {selected_placement}")
                continue
            return turn

    def get_build(self):
        while True:
            selected_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n").lower()
            if selected_build not in DIRECTION_TRANSFORMATION:
                print("Not a valid direction")
                continue
            if selected_build not in self._valid_builds:
                print(f"Cannot build {selected_build}")
                continue
            return selected_build

    def get_valid_turn(self, worker, potential_placement):
        for turn in self._valid_placements:
            if turn.worker == worker and turn.placement_direction == potential_placement:
                #turn.build_transformation_coordinate = DIRECTION_TRANSFORMATION[potential_placement]
                return turn
        return None
        
    def build_turn(self, board):
        
        self._build_valid_placements(board)
        valid_worker = self.get_worker(board.workers)

        turn = self.get_placement(valid_worker)

        self._build_valid_builds(turn, board)
        build_direction = self.get_build()
        turn.build_direction = build_direction
        turn.build_transformation_coordinate = DIRECTION_TRANSFORMATION[build_direction]
        turn.calc_build_coordinate()

        return turn

class AIPlayer(Player):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self):
        pass

    def get_build(self):
        return choice(self._valid_builds)

    def build_turn(self, board):
        self._build_valid_placements(board)
        turn = self.get_player_and_placement()
        self._build_valid_builds(turn, board)
        build_direction = self.get_build()
        turn.build_direction = build_direction
        turn.build_transformation_coordinate = DIRECTION_TRANSFORMATION[build_direction]
        turn.calc_build_coordinate()

        return turn        

class AIRandomPlayer(AIPlayer):

    def get_player_and_placement(self):
        return choice(self._valid_placements)

class AIHeuristicPlayer(AIPlayer):
    def get_player_and_placement(self):
        return max(self._valid_placements, key=self._valid_placements.move_score.total_score)
    #     max_move_score = 0
    #     best_placement = None

    #     for placement in self._valid_placements:
    #         # calculate height score, center score, distance score
    #         height_score = self._calculate_height_score(placement)
    #         center_score = self._calculate_center_score(placement)
    #         distance_score = self._calculate_distance_score(placement)

    #         # calculate move score using the given weights
    #         move_score = 3 * height_score + 2 * center_score + 1 * distance_score

    #         # update max_move_score and best_placement if the current placement has a higher move score
    #         if move_score > max_move_score:
    #             max_move_score = move_score
    #             best_placement = placement

    #     # Return the best turn with the maximum move score
    #     return best_placement