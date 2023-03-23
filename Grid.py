from Cell import Cell

import time


class Grid():

    def __init__(self, height, width, shatter=None, convert=None, values=None):

        #optimization constants:
        hm1 = height - 1
        wm1 = width - 1

        self.grid = []
        self.active_cells = set()
        self.height = height
        self.width = width

        self.tick = 0

        # populate grid with cells
        print("[Grid] Populating grid with cells...")
        start_time = time.time()
        for h in range(height):
            row = []
            for w in range(width):
                # if values is not None:
                #     row.append(Cell(h,w, value=values[h][w]))
                # else:
                row.append(Cell(h,w))

            self.grid.append(row)
        print(f"\t ...Done! time: {time.time() - start_time}")

        # set up cell associations
        print("[Grid] Setting up cell associations...")
        start_time = time.time()
        for h in range(height):
            for w in range(width):

                current_cell = self.grid[h][w]

                if w != 0:
                    current_cell.neighbors['L'] = self.grid[h][w - 1]

                if w != wm1:
                    current_cell.neighbors['R'] = self.grid[h][w + 1]

                if h != 0:
                    current_cell.neighbors['T'] = self.grid[h - 1][w]

                if h != hm1:
                    current_cell.neighbors['B'] = self.grid[h + 1][w]

        print(f"\t ...Done! time: {time.time() - start_time}")

        # if values is not None:
        #     # load active nodes since this is a resume job (Unimplemented)
        #     middle_row = self.grid[height//2]
        #
        #     edge = None
        #     for index, cell in enumerate(middle_row):
        #         if cell.get_value() != 0:
        #             edge = index - 3 if index >= 3 else 0
        #             break
        #
        #     # count how far away the cell is from the middle cell
        #     dist = self.width//2 - edge.w
        #
        #     # since this edge cell is in the middle, top corner of active cells will be at point (edge.w, edge.h-dist)
        #     top_left = self.grid[edge.w][edge.h - dist]
        #     for h in range(top_left.h, top_left.h + 2*dist):
        #         for w in range(top_left.w, top_left.w + 2*dist):
        #             self.active_cells.add(self.grid[h][w])


    def iterate(self):
        found_unstable = False
        self.tick += 1
        # print(f"Tick: {self.tick} found: {len(self.active_cells)} active cells. ")
        for c in self.active_cells.copy():
            # print(f"Cell: [{c.h}:{c.w}] value: {c.value} is_stable: {c.is_stable()}")
            if c.shatter(): # TODO need to define a different shatter method for cells. perhaps in Grid allow a cell to have a shatter method passed in.
                neighbors = c.get_neighbors()
                for n in neighbors:
                    self.active_cells.add(n)
                found_unstable = True
        if found_unstable:
            for c in self.active_cells:
                c.convert() # TODO need to define a different convert method for cells. perhaps in Grid allow a cell to have a shatter method passed in.

        return found_unstable

    def export(self):
        ret = []
        board_total = 0
        for h in range(self.height):
            row = []
            for w in range(self.width):
                val = self.grid[h][w].get_value()
                board_total += val
                row.append(val)
            ret.append(row)

        print("Board total: " + str(board_total))

        return ret

    def set_cell_value(self, h, w, value):
        self.grid[h][w].set_value(value)
        self.active_cells.add(self.grid[h][w])
