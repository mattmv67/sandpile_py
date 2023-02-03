
class Cell():

    def __init__(self, h, w, value=0,  max_cap=4):
        self.value = value
        self.max_cap = max_cap
        self.buffer = 0

        self.h = h
        self.w = w
        self.neighbors = []it bash

    def __eq__(self, other):
        return self.h == other.h and self.w == other.w

    def __hash__(self):
        return hash(f"{self.h}:{self.w}")


    def is_stable(self):
        return self.value < self.max_cap

    def stack(self):
        self.buffer += 1

    def shatter(self):
        if not self.is_stable():
            self.buffer -= self.max_cap
            for n in self.neighbors:
                n.stack()
            return True
        return False

    def convert(self):
        self.value += self.buffer
        self.buffer = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_neighbors(self):
        return self.neighbors