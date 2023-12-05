class Cell:
    """Class representing a cell on the Santorini game board"""

    def __init__(self, height, worker_character):
        self._height = height
        self._worker_character = worker_character

    def __str__(self):
        return f"{self._height}{self._worker_character}"