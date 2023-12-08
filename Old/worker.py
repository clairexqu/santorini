class Worker:
    """
    Define a worker class, with a char and a location.
    """

    def __init__(self, char, row, col):
        self._char = char
        self._location = [row, col]

    def _set_location(self, row, col):
        """Set the location of the worker."""
        self._location = [row, col]
    
    def __str__(self):
        """Return the current board state."""
        return str(self._char)