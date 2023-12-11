class Cell:
    """Class representing a cell on the Santorini game board, with a height and a worker, if any."""
    def __init__(self, height, worker_character):
        self.height = height
        self.worker_character = worker_character

    def __str__(self):
        """Returns the current state of a cell."""
        return f"{self.height}{self.worker_character}"