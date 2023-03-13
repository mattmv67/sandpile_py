
class Cell():

    def __init__(self, h, w, value=0,  max_cap=4):
        self.value = value
        self.max_cap = max_cap
        self.buffer = 0
        self.critical = value > max_cap
        self.h = h
        self.w = w
        self.neighbors =  {}

        # self.team = None

    def __eq__(self, other):
        return self.h == other.h and self.w == other.w

    def __hash__(self):
        return hash(f"{self.h}:{self.w}")


    def is_stable(self):
        return self.value < self.max_cap

    def add_buffer(self, val, is_crit):
        self.buffer += val if not is_crit else val*2

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

    def set_critical(self, boo):
        self.critical = boo

    def get_critical(self):
        return self.critical
    #
    # def get_team(self):
    #     return self.team
    #
    # def set_team(self, team):
    #     self.team = team