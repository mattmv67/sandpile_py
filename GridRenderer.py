from PIL import Image
import random
import time

from SingleGameContainer64x128 import SingleGameContainer64x128



class GridRenderer:

    def __init__(self, *grids, color_map=None):
        self.grids = grids

        self.color_map = {
            0: (0, 0, 0),   # Black
            1: (245, 221, 66),
            2: (245, 120, 66),
            3: (245, 66, 66),
            -1: (66, 245, 245),
            -2: (66, 158, 245),
            -3: (66, 66, 245),
            "POS_UNSTABLE": (245, 0, 66),
            "NEG_UNSTABLE": (66, 0, 245),
            "BACKGROUND_COLOR": (81, 137, 14)
        }

        if self.color_map is None:
            self.color_map = COLOR_MAP

                

        
        
        
        # ==Chat GPT side quest==
        # self.width = len(self.grids[0][0])
        # self.height = len(self.grids[0])
        # self.grid_distance = 100
        # self.grid_width = (1920 - 4 * self.grid_distance) // 3
        # self.image_width = 1920
        # self.image_height = 1080
        # self.image = Image.new('RGB', (self.image_width, self.image_height), self.BACKGROUND_COLOR)

    def create_image(self):
        
        g_len = len(self.grids)
        bgrs = []
        if g_len == 1:
            bgrs = SingleGameContainer64x128(self.grids[0], self.color_map).capture()
        
        return bgrs
        
        
        ''' === Chat GPT Side quest ===
        # Determine the scale factor to fit the image into the available space
        num_grids = len(self.grids)
        total_grid_width = 3 * self.grid_width + 2 * self.grid_distance
        scale_factor = min((self.image_height - 3 * self.grid_distance) / 2 / self.height, total_grid_width / self.width)

        # Add each grid to the image
        for i, grid in enumerate(self.grids):
            grid_image = Image.new('RGB', (self.width, self.height))
            pixels = grid_image.load()
            for y in range(self.height):
                for x in range(self.width):
                    pixels[x, y] = self.COLOR_MAP.get(grid[y][x], (255, 255, 255))
            x_pos = int((self.image_width - total_grid_width) / 2 + i % 3 * (self.grid_width + self.grid_distance) + (self.grid_width - scale_factor * self.width) / 2)
            y_pos = int((self.image_height - 2 * self.grid_distance) // 2 + i // 3 * (self.height + self.grid_distance) + (self.height - scale_factor * self.height) / 2)
            self.image.paste(grid_image.resize((int(scale_factor * self.width), int(scale_factor * self.height))), (x_pos, y_pos))

        return self.image'''




if __name__ == '__main__':  #r debug pru
    random.seed(time.time())

    # Generate random grids
    grids = []
    for i in range(1):
        grid = [[random.randint(-3, 3) for x in range(64)] for y in range(128)]
        grids.append(grid)

    # Create the grid image
    grid_image = GridRenderer(*grids)

    # Generate the image
    image = grid_image.create_image()

    # Display the image
    image.show()