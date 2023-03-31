import numpy as np
import cv2
import imutils


class SingleGameContainer64x128:

    def __init__(self, grid, color_map):
        self.grid = grid
        self.color_map = color_map
        

    def capture(self):

        # Define input list
        input_list = [[self.color_map[cell if cell in self.color_map else "POS_UNSTABLE" if cell > 0 else "NEG_UNSTABLE"] for cell in grid_row] for grid_row in self.grid]

        # Convert 2D Python list to NumPy array
        input_list = np.array(input_list, dtype=np.uint8)

        # Print shape of resulting array
        print(input_list.shape)

        # Define size of output image
        output_height = 1080
        output_width = 1920

        # Define size of input list
        input_height = len(input_list)
        input_width = len(input_list[0])

        # Compute scaling factor to fit input list into output image
        scale_factor = min(output_width/input_width, output_height/input_height)

        # Compute new dimensions for input list
        new_input_height = int(input_height * scale_factor)
        new_input_width = int(input_width * scale_factor)

        # Compute offset to center input list in output image
        offset_height = (output_height - new_input_height) // 2
        offset_width = (output_width - new_input_width) // 2

        # Create empty output image
        output_image = np.zeros((output_height, output_width, 3), dtype=np.uint8)

        # Resize and center input list in output image
        # resized_input = cv2.resize(np.array(input_list), (new_input_width, new_input_height))
        resized_input = imutils.resize(input_list, width=new_input_width, height=new_input_height) 
        output_image[offset_height:offset_height+new_input_height, offset_width:offset_width+new_input_width, :] = resized_input

        # Save output image
        # cv2.imwrite("output_image.jpg", output_image)
        return output_image



if __name__ == '__main__':

    import random

    COLOR_MAP = { # BGR format WTF cv2?
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

    grid = []

    for h in range(128):
        grid_row = []
        for w in range(64):
            grid_row.append(random.randint(-6,6))
        grid.append(grid_row)

    s = SingleGameContainer64x128(grid, COLOR_MAP)

    rgbs = s.capture()


