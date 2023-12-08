from worker import Worker 

class Player:
    def __init__(self, color, workers):
        """
        Define a general player of the game, from which the actual players
        will inherit (template).
        """
        self._color = color
        self._workers = workers

    def create_move(self):
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

    def get_player(self):
        input("Select a worker to move")

    def get_placement(self):
        input("Select a direction to move (n, ne, e, se, s, sw, w, nw)")

    def get_build(self):
        input("Select a direction to build (n, ne, e, se, s, sw, w, nw)")

    def create_move(self):
        # IMPLEMENT
        pass


class AIPlayer(Player):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self):
        pass

    def build():
        pass

    # IMPLEMENT random build

    def create_move(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AIHeuristic(AIPlayer):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # IMPLEMENT

    def build(self):
        pass

    def create_move(self):
        pass


class AIRandom(AIPlayer):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    def get_player_and_placement(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # IMPLEMENT

    def build(self):
        pass

    def create_move(self):
        pass
