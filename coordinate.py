class Coordinate:
    """Class representing a coordinate, with a row and a column."""

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __add__(self, other):
        """Does coordinate addition. Adsd the rows and columns of two coordinates, returning a Coordinate object.
        Useful for adding a transformation coordinate to a coordinate that represents a location
        """
        new_row = self.row + other.row
        new_column = self.column + other.column
        return Coordinate(new_row, new_column)


# FINAL DRAFT
