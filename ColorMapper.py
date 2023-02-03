

class ColorMapper:

    standard = {
        0: (157, 2, 255),
        1: (182, 57, 191),
        2: (206, 112, 128),
        3: (231, 167, 64),
        "default": (255, 222, 0)
    }

    def __init__(self, raw_data, mapping=None):

        self.raw_data = raw_data

        if mapping is None:
            self.mapping = self.standard
        else:
            self.mapping = mapping

    def map(self):

        ret = []

        for each in self.raw_data:
            row = []
            for value in each:
                row.append(self.mapping[value] if value in self.mapping else self.mapping["default"])
            ret.append(row)
        return ret
