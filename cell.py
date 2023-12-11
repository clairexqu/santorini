class Cell:
    """Class representing a cell on the Santorini game board"""
    def __init__(self, height, worker_character):
        self.height = height
        self.worker_character = worker_character

# how to print cell such that we check for if it has a worker?
    def __str__(self):
        return f"{self.height}{self.worker_character}"