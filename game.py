from board import Board
from player import HumanPlayer
from turn_commands import TurnBuilderCommand#, DoTurnCommand

class Game:
    """Class representing the Santorini game"""

    def __init__(self):
        self._board = Board()
        self.enable_undo_redo = False 
        self.enable_score_display = False 

        self.player1 = HumanPlayer("white", ['A', 'B'])
        self.player2 = HumanPlayer("blue", ['Y', 'Z'])
        self.players = [self.player2, self.player1]
        self.turn = 1

    def create_player():
        pass

    def execute_turn(self):
        #self._print_turn_info()

        # Build the move
        current_player = self._current_player()
        
        #self._print_turn_info()
        #print(str(current_player))

        turn_builder_command = TurnBuilderCommand(self._board, current_player)
        turn_builder_command.execute()

        turn = turn_builder_command.get_turn()

        print(str(turn))

        #move = move_builder_command.get_move()
        # Execute the move
        #move_command = MoveCommand(board, move)
        #move_command.execute()
        
        self.turn = self.turn + 1
        #move = players[self.turn % 2].build_turn() #send in own workers and other players works 
        #self._board.update_board()
        #pass 

    def _current_player(self):
        return self.players[self.turn % 2]
        
    def __str__(self):
        # USE THIS EVENTUALLY 
        game_str = ""
        game_str += f"{str(self._board)}\nTurn: {str(self.turn)}, {str(self._current_player())}"
        return game_str
    
    # def _print_turn_info(self):
    #     print("Turn: " + str(self.turn) + " player: " + str(self.turn % 2) + "\n")
    #     pass


    def print_board(self):
        print(str(self._board))

    def is_game_over(self):
        if self.turn == 3:
            return True
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

# IMPLEMENT validate moves