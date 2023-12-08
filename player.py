from turn import Turn

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
        return input("Select a worker to move\n")

    def get_placement(self):
        return input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")

    def get_build(self):
        return input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")

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
