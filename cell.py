class Cell:
    """Class representing a cell on the Santorini game board, with a height and a character representing a worker, if any."""

    def __init__(self, height, worker_character):
        self.height = height
        self.worker_character = worker_character

    def __str__(self):
        """Returns a string of the cell consisting of the height and the character representing a worker, if any.
        Represents the current state of the cell"""
        return f"{self.height}{self.worker_character}"


# FINAL DRAFT
