from SingleCenterValue import SingleCenterValue

from PIL import Image

def get_pixels(filename):
    img = Image.open(filename, 'r')
    w, h = img.size
    pix = list(img.getdata())
    return [pix[n:n+w] for n in range(0, w*h, w)]

def resume(image_filename, sandpile):

    1#first load our image into pixel RGB values
    pixels = get_pixels(image_filename)

    values = []
    # Map pixel values to their numerical form

    print("Beginning value mapping")
    for row in pixels:
        value_row = []
        for rgb in row:
            for value, color in sandpile.color_mapping.items():
                if rgb == color:
                    value_row.append(value)
            values.append(value_row)
    print("Beginning value mapping")

    sandpile = SingleCenterValue(sandpile.height, sandpile.width, sandpile.initial_value, values=values)
    sandpile.generate()
if __name__ == '__main__':


    color_dict = {
        0: (0, 0, 0),
        1: (118, 48, 234),
        2: (206, 112, 128),
        3: (255, 131, 0),
        "default": (254, 201, 1)
    }

    sandpile = SingleCenterValue(1920, 1920, 800000)
    resume("static/test.png", sandpile)
