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
        self._own_workers = workers

    def build_turn(self, turn, board):
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

    def get_worker(self, workers_dict):
        while True:
            selected_worker = input("Select a worker to move\n").upper()
            if selected_worker not in workers_dict:
                print("Not a valid worker")
                continue
            elif selected_worker not in self._own_workers:
                print("That is not your worker")
                continue
            return selected_worker
        # return input("Select a worker to move\n").upper()

    def get_placement(self):
        while True:
            selected_placement = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n").lower()
            if selected_placement not in DIRECTION_TRANSFORMATION:
                print("Not a valid direction")
                continue
        # CHECK FOR VALID DIRECTION: "Cannot move <direction>"
            return selected_placement
        # return input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n").lower()

    def get_build(self):
        while True:
            selected_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n").lower()
            if selected_build not in DIRECTION_TRANSFORMATION:
                print("Not a valid direction")
                continue
        # CHECK FOR VALID DIRECTION: "Cannot build <direction>"
            return selected_build
        
    def build_turn(self, turn, board):
        turn.worker = self.get_worker(board.workers)
        
        turn.placement_direction = self.get_placement()
        turn.placement_transformation_coordinate = DIRECTION_TRANSFORMATION[turn.placement_direction]
        #print(str(turn.placement_transformation_coordinate))

        turn.build_direction = self.get_build()
        turn.build_transformation_coordinate = DIRECTION_TRANSFORMATION[turn.build_direction]
        #print(str(turn.build_transformation_coordinate))
        


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
