

class HumanPlayer:

    def __init__(self, p_name, p_team, pre_moves=[]):
        self.team = p_team
        self.name = p_name
        self.pre_moves = pre_moves


    def get_team(self):
        return self.team

    def play(self, board_data, points):

        if len(self.pre_moves) != 0:
            return self.pre_moves.pop(0)


 
        while points > 0:
            print(f"{self.name}, it is your turn. Here is the current state of the board:\n")


            for h in range(len(board_data)):
                row_str = f"{h:^3}: |"
                for w in range(len(board_data[h])):
                    row_str += f"{board_data[h][w].get_value():^3}|"
                print(row_str)

            p_h = None
            while True:
                try:
                    p_h = int(input(f"You have '{points}' points to spend. Please select the row to add value to: "))
                    break
                except:
                    print("invalid input")

            p_row = board_data[p_h]


            row_str = f"{p_h:^3}: |"
            for w in range(len(p_row)):
                row_str += f"{board_data[p_h][w].get_value():^3}|"
            
            row_str += f"\n{' ':^5}"
            for w in range(len(p_row)):
                row_str += f"{w:^4}"
            
            print("\n\n" + row_str)

            p_w = None
            while True:
                try:
                    p_w = int(input(f"You have '{points}' points to spend. Please select the cell to add value to: "))
                    break
                except:
                    print("invalid input")


            val = None
            while True:
                try:
                    val = int(input(f"You have '{points}' points to spend. Please select the cell to add value to: "))
                    break
                except:
                    print("invalid input")

            points -= val

            move.append(((p_h, p_w), val))

        return move
        