

class Player:
    def __init__(self):
        """
        Define a general player of the game, with a strategy, a color,
        and 2 workers.
        """
        # self._color = color
        # self._worker1 = worker1
        # self._worker2 = worker2

    def next_move(self):
        pass

    def build(self):
        pass

class HumanPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def next_move(self):
        pass
#IIMPLEMENT

    def build(self):
        pass

    

class AIPlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def next_move(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build():
        pass

class AIHeuristic(AIPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def next_move(self):
        pass

    def build(self):
        pass

class AIRandom(AIPlayer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)