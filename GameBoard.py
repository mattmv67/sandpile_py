from Sandpile import Sandpile
from Grid import Grid
import json

class GameBoard(Grid):

    def __init__(self, player_1, player_2, config_file='game_config.json' ):

        self.config = None
        with open(config_file) as json_file:
            self.config = json.load(json_file)

        self.player_1 = player_1
        self.player_2 = player_2

        # Sets up cell grid and cell associations.
        super(GameBoard, self).__init__(self.config['BoardHeight'], self.config['BoardWidth'])

    def play(self):
        while self.in_progress():
            for player in [self.player_1, self.player_2]:
                move = player.play(self.export_game_data())
                p_team = player.get_team()
                self.add_to_values(move)
                marked_cells = self.mark_unstable_enemies(p_team)
                self.shatter(p_team)
                self.unmark_cells(marked_cells)
                self.convert()


    def in_progress(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.grid[h][w].get_value() > 3:
                    return True

        return False


    def add_to_values(self, p_move):
        cells = p_move['cells']

        for each_tup in cells: # each_tup: ((h,w), value)
            c = self.grid[each_tup[0][0]][each_tup[0][1]]
            cell_value = c.get_value()
            move_value = each_tup[1]
            c.set_value(cell_value + move_value)


    def mark_unstable_enemies(self, p_team):
        unstable_cells = []
        for h in range(self.height):
            for w in range(self.width):
                c = self.grid[h][w]
                c_value = c.get_value()
                if abs(c_value) > 3 and c_value * p_team < 0: # TODO perhaps an else clause that stores the other nodes so we can return a list of them instead of looking again
                    # if c is unstable and an enemy cell
                    c.set_critical(True)
                    unstable_cells.append(c)
        return unstable_cells

    def shatter(self, p_team):
        for h in range(self.height):
            for w in range(self.width):
                c = self.grid[h][w]
                c_value = c.get_value()
                if abs(c_value) > 3 and c_value * p_team > 0 :
                    ns = c.get_neighbors()
                    ns_len = len(ns)
                    if ns_len == 4:
                        for _, nv in ns.items():
                            nv.add_buffer(p_team, nv.get_critical())
                    elif ns_len == 3: # TODO optimize this...
                        if not 'T' in ns:
                            ns['L'].add_buffer(p_team, ns['L'].get_critical)
                            ns['B'].add_buffer(p_team*2, ns['B'].get_critical)
                            ns['R'].add_buffer(p_team, ns['R'].get_critical)
                        elif not 'B' in ns:
                            ns['L'].add_buffer(p_team, ns['L'].get_critical)
                            ns['T'].add_buffer(p_team * 2, ns['T'].get_critical)
                            ns['R'].add_buffer(p_team, ns['R'].get_critical)
                        elif not 'L' in ns:
                            ns['T'].add_buffer(p_team, ns['T'].get_critical)
                            ns['R'].add_buffer(p_team * 2, ns['R'].get_critical)
                            ns['B'].add_buffer(p_team, ns['B'].get_critical)
                        else:
                            ns['B'].add_buffer(p_team, ns['B'].get_critical)
                            ns['L'].add_buffer(p_team * 2, ns['L'].get_critical)
                            ns['T'].add_buffer(p_team, ns['T'].get_critical)
                    else:
                        for _, nv in ns.items():
                            nv.add_buffer(p_team*2, nv.get_critical())

    def convert(self):
        for h in range(self.height):
            for w in range(self.width):
                self.grid[h][w].convert()

    def unmark_cells(self, cells):
        for c in cells:
            c.set_critical(False)



    def iterate_game(self, team):
        found_unstable = False
        self.tick += 1
        for c in self.active_cells.copy(): #TODO investigate copy???
            if not c.is_stable():
                found_unstable = True
                neighbors = c.get_neighbors()

                c_team = c.get_team()

                for n in neighbors:
                    n_team = n.get_team()

                    if n_team == c_team * -1: #enemy team
                        if n.is_unstable
                    else:
                        n.set_team(c_team)






            if c.shatter():
                neighbors = c.get_neighbors()
                for n in neighbors:
                    self.active_cells.add(n)
                found_unstable = True
        if found_unstable:
            for c in self.active_cells:
                c.convert()

        return found_unstable


    def export_game_data(self):
        team_value_pairs = []
        team_1_unstable = 0
        team_2_unstable = 0
        team_3_unstable = 0

        for h in range(self.height):
            row = []
            for w in range(self.width):
                c = self.grid[h][w]
                team = c.get_team()

                row.append((team, c.get_value()))
                if (not c.is_stable()):
                    if team == 0:
                        team_3_unstable += 1
                    elif team == -1:
                        team_2_unstable += 1
                    else:
                        team_1_unstable += 1

            team_value_pairs.append(row)

        return self.tick, team_value_pairs, (team_1_unstable, team_2_unstable, team_3_unstable)

