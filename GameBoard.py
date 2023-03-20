from Sandpile import Sandpile
from GridRenderer import GridRenderer
from MP4VideoWriter import MP4VideoWriter
from Grid import Grid
import json

class GameBoard(Grid):

    def __init__(self, player_1, player_2, config_file='game_config.json' ):

        self.config = None
        with open(config_file) as json_file:
            self.config = json.load(json_file)

        self.player_1 = player_1
        self.player_2 = player_2

        self.bonus_dict = {}

        self.video_writer = MP4VideoWriter("game.mp4", 20)

        # Sets up cell grid and cell associations.
        super(GameBoard, self).__init__(self.config['BoardHeight'], self.config['BoardWidth'])

    def play(self):

        round_bonus = 16
        num_bonuses = 50

        self.bonus_dict = {
            self.player_1.name: 0,
            self.player_2.name: 0
        }

        for player in [self.player_1, self.player_2]:
            move = player.play(self.grid, round_bonus)
            p_team = player.get_team()
            self.add_to_values(move, p_team)
            marked_cells = self.mark_unstable_enemies(p_team)
            shatter_bonus = self.shatter(p_team)
            self.bonus_dict[player.name] = shatter_bonus
            self.unmark_cells(marked_cells)
            self.convert()

        self.tick += 1

        while self.in_progress():
            print("Tick: " + str(self.tick))
            for player in [self.player_1, self.player_2]:
                move = player.play(self.grid, (round_bonus if self.tick < num_bonuses else 0) + self.bonus_dict[player.name]//16)
                p_team = player.get_team()
                self.add_to_values(move,p_team)
                marked_cells = self.mark_unstable_enemies(p_team)
                shatter_bonus = self.shatter(p_team)
                self.bonus_dict[player.name] = shatter_bonus
                self.unmark_cells(marked_cells)
                self.convert()
            self.tick += 1
            image = GridRenderer(self.export()).create_image()
            self.video_writer.add_frame(image)

        self.video_writer.export_video();



    def in_progress(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.grid[h][w].get_value() > 3 and not (self.bonus_dict[self.player_1.name] == 0 and self.bonus_dict[self.player_2.name] == 0):
                    return True
        return False


    def add_to_values(self, cells, p_team):

        for each_tup in cells: # each_tup: ((h,w), value)
            c = self.grid[each_tup[0][0]][each_tup[0][1]]
            cell_value = c.get_value()
            move_value = each_tup[1] * p_team
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

        bonus = 0

        for h in range(self.height):
            for w in range(self.width):
                c = self.grid[h][w]
                c_value = c.get_value()

                if abs(c_value) > 3 and c_value * p_team > 0 :
                    # if c is unstable and friendly cell
                    bonus += 1
                    ns = c.get_neighbors()
                    ns_len = len(ns)
                    if ns_len == 4:
                        for _, nv in ns.items():
                            nv.add_buffer(p_team, nv.get_critical())
                    elif ns_len == 3: # TODO optimize this...
                        if not 'T' in ns:
                            ns['L'].add_buffer(p_team, ns['L'].get_critical())
                            ns['B'].add_buffer(p_team*2, ns['B'].get_critical())
                            ns['R'].add_buffer(p_team, ns['R'].get_critical())
                        elif not 'B' in ns:
                            ns['L'].add_buffer(p_team, ns['L'].get_critical())
                            ns['T'].add_buffer(p_team * 2, ns['T'].get_critical())
                            ns['R'].add_buffer(p_team, ns['R'].get_critical())
                        elif not 'L' in ns:
                            ns['T'].add_buffer(p_team, ns['T'].get_critical())
                            ns['R'].add_buffer(p_team * 2, ns['R'].get_critical())
                            ns['B'].add_buffer(p_team, ns['B'].get_critical())
                        else:
                            ns['B'].add_buffer(p_team, ns['B'].get_critical())
                            ns['L'].add_buffer(p_team * 2, ns['L'].get_critical())
                            ns['T'].add_buffer(p_team, ns['T'].get_critical())
                    else:
                        for _, nv in ns.items():
                            nv.add_buffer(p_team*2, nv.get_critical())
                    c.set_value(c_value- (4*p_team))
        
        return bonus


    def convert(self):
        for h in range(self.height):
            for w in range(self.width):
                self.grid[h][w].convert()

    def unmark_cells(self, cells):
        for c in cells:
            c.set_critical(False)

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

                row.append((c.get_value()))
                if (not c.is_stable()):
                    if team == 0:
                        team_3_unstable += 1
                    elif team == -1:
                        team_2_unstable += 1
                    else:
                        team_1_unstable += 1

            team_value_pairs.append(row)

        return self.tick, team_value_pairs, (team_1_unstable, team_2_unstable, team_3_unstable)

