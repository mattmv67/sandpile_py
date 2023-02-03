from Sandpile import Sandpile
from Grid import Grid
from ColorMapper import ColorMapper
from Renderer import Renderer


class SingleCenterValue(Sandpile):
    DEFAULT_COLOR_MAP = {
        0: (157, 2, 255),
        1: (182, 57, 191),
        2: (206, 112, 128),
        3: (231, 167, 64),
        "default": (255, 222, 0)
    }

    def __init__(self, height: int, width: int, initial_value, values=None, color_mapping={0: (157, 2, 255),1: (182, 57, 191),2: (206, 112, 128),3: (231, 167, 64),"default": (255, 222, 0)}):

        # Build Grid object. using resolution
        # Grid object will track the value of cells
        # Grid is also responsible for generating and transitioning to each "tick" of the fractal
        # Grid will be able to return a 2D array of cell values
        hd2 = height//2
        wd2 = width//2

        self.height = height
        self.width = width
        self.color_mapping = color_mapping
        self.initial_value = initial_value

        self.grid = Grid(height, width, values=values)
        self.grid.set_cell_value(height//2, width//2, initial_value)




    def generate(self):
        hd2 = self.height // 2
        wd2 = self.width // 2

        while self.grid.iterate():
            if self.grid.tick % 100 == 0:
                print(f"CenterCell: {self.grid.grid[hd2][wd2].value}")
                raw = self.grid.export()

                rgbs = ColorMapper(raw).map()

                Renderer(rgbs).render()
            pass

        raw = self.grid.export()

        rgbs = ColorMapper(raw, color_mapping).map()

        Renderer(rgbs).render()