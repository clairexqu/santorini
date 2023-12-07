from playerstrategy import PlayerStrategy


class Player:
    """
    Define a general player of the game, with a strategy, a color,
    and 2 workers.
    """
    def __init__(self, strategy: PlayerStrategy):
        self._strategy = strategy
        # self._color = 

