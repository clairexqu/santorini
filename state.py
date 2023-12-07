import sys

from board import Board


class GameState:
    """Base class for game states."""

    def handle_input(self, game):
        raise NotImplementedError()

    def update(self, game):
        raise NotImplementedError()


class PlacementState(GameState):
    """State representing the worker placement phase."""

    def handle_input(self, game):
        worker = input("Select a worker to place: ")
        position = input("Select a position to place the worker (row column): ")
        row, col = map(int, position.split())
        game.place_worker(worker, row, col)

    def update(self, game):
        if game.is_placement_complete():
            game.set_state(BuildingState())


class BuildingState(GameState):
    """State representing the building phase."""

    def handle_input(self, game):
        position = input("Select a position to build (row column): ")
        row, col = map(int, position.split())
        game.build_level(row, col)

    def update(self, game):
        if game.is_building_complete():
            game.set_state(MovementState())


class MovementState(GameState):
    """State representing the movement phase."""

    def handle_input(self, game):
        worker = input("Select a worker to move: ")
        direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw): ")
        game.move_worker(worker, direction)

    def update(self, game):
        if game.is_game_over():
            game.set_state(GameOverState())


class GameOverState(GameState):
    """State representing the game over phase."""

    def handle_input(self, game):
        choice = input("The game is over. Would you like to play another game? (yes/no): ")
        if choice.lower() == "yes":
            game.reset()
            game.set_state(PlacementState())
        else:
            sys.exit(0)

    def update(self, game):
        pass


class Game:
    """Class representing the Santorini game"""

    def __init__(self):
        self._board = Board()
        self._state = PlacementState()

    def place_worker(self, worker, row, col):
        # Implement worker placement logic
        pass

    def build_level(self, row, col):
        # Implement building logic
        pass

    def move_worker(self, worker, direction):
        # Implement worker movement logic
        pass

    def is_placement_complete(self):
        # Implement logic to check if worker placement is complete
        pass

    def is_building_complete(self):
        # Implement logic to check if building phase is complete
        pass

    def is_game_over(self):
        # Implement logic to check if the game is over
        pass

    def reset(self):
        # Reset the game state
        pass

    def set_state(self, state):
        self._state = state

    def run(self):
        """Start the game with the provided board state."""

        while True:
            print(str(self._board))
            self._state.handle_input(self)
            self._state.update(self)


if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except Exception as e:
        print("Sorry! Something unexpected happened.")
        sys.exit(0)