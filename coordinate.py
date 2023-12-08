class Coordinate:
    def __init__(self, row, column):
        self.row = row
        self.column = column

# testing purposes 
    def __str__(self):
        """Return the current board state."""
        coordinate_str = f"Row: {str(self.row)} Column: {str(self.column)}"
        return coordinate_str
