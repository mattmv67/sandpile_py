from Grid import Grid

class Sandpile:

    def __init__(self, height: int, width: int, initial_value, values=None, color_mapping={0: (157, 2, 255),1: (182, 57, 191),2: (206, 112, 128),3: (231, 167, 64),"default": (255, 222, 0)}):

        # Build Grid object. using resolution
        # Grid object will track the value of cells
        # Grid is also responsible for generating and transitioning to each "tick" of the fractal
        # Grid will be able to return a 2D array of cell values
        self.height = height
        self.width = width
        self.color_mapping = color_mapping
        self.grid = Grid(height, width, values=values)

        self.height = height
        self.width = width