import abc


class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy()

    def set_strategy(self, strategy):
        self._strategy = strategy



class PlayerStrategy(metaclass=abc.ABCMeta):
    """
    Player uses this interface to call the algorithm defined by
    a Concrete Strategy.
    """

    @abc.abstractmethod
    def __call__(self):
        pass


class ConcreteStrategyHuman(PlayerStrategy):
    """
    Implement the human player's algorithm using the Strategy interface.
    """

    def next_move(self, direction, build):
        print("A")
        # shoudl a move be created here / for all of these? how does that work with the command pattern


class ConcreteStrategyRandom(PlayerStrategy):
    """
    Implement the random player's algorithm using the Strategy interface.
    """

    def next_move(self):
        pass

class ConcreteStrategyHeuristic(PlayerStrategy):
    """
    Implement the heuristic player's algorithm using the Strategy interface.
    """

    def next_move(self):
        pass


# def main():
#     concrete_strategy_a = ConcreteStrategyA()
#     context = Context(concrete_strategy_a)
#     context.context_interface()

#     context.set_strategy(ConcreteStrategyB())
#     context.context_interface()

#     context = Context(strategy_b)
#     context.context_interface()

#     context2 = strategy_a
#     context2()
#     context2 = strategy_b
#     context2()


# if __name__ == "__main__":
#     main()