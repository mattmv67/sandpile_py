import random
import time

class RandomFirstRowPlayer:

    def __init__(self, p_name, p_team, row_index=0):
        self.team = p_team
        self.name = p_name
        self.row_index = row_index
        random.seed(time.time())


    def get_team(self):
        return self.team

    def play(self, board_data, points):

        move = []

        while points > 0:
            to_spend = random.randint(1, points)
            
            ran_w = random.randint(0, len(board_data[self.row_index])-1)

            move.append(((self.row_index, ran_w), to_spend))

            points -= to_spend
        print(self.name + " returning move; " +  str(move))

        return move
        