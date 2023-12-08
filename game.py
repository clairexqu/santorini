from board import Board

class Game:
    """Class representing the Santorini game"""

    def __init__(self):
        self._board = Board()
        self.player1 = None
        self.player2 = None 
        self.players = [self.player1, self.player2]
        self.turn = 0

    def execute_turn(self):
        move = players[self.turn % 2].build_turn() #send in own workers and other players works 
        self._board.update_board()
        pass 
  
    def is_game_over(self):
        return False 

    # def place_worker(self, worker, row, col):
    #     # Implement worker placement logic
    #     pass

    # def build_level(self, row, col):
    #     # Implement building logic
    #     pass

    # def move_worker(self, worker, direction):
    #     # Implement worker movement logic
    #     pass

    # def is_placement_complete(self):
    #     # Implement logic to check if worker placement is complete
    #     pass

    # def is_building_complete(self):
    #     # Implement logic to check if building phase is complete
    #     pass

    # def is_game_over(self):
    #     # Implement logic to check if the game is over
    #     pass

    # def reset(self):
    #     # Reset the game state
    #     pass
