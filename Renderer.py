import numpy as np
from PIL import Image  # Pillow


class Renderer:

    def __init__(self, rgbs, output_filename="static/test.png"):
        self.rgbs = rgbs
        self.output_filename = output_filename


    def render(self):
        img = Image.fromarray(np.asarray(self.rgbs, dtype=np.uint8))
        img.save(self.output_filename)
