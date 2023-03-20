from GameBoard import GameBoard
from HumanPlayer import HumanPlayer
from RandomFirstRowPlayer import RandomFirstRowPlayer



if __name__ == '__main__':
    
    player_1 = RandomFirstRowPlayer("Player 1", 1, 0)
    player_2 = RandomFirstRowPlayer("Player 2", -1, 127)
    
    board = GameBoard(player_1, player_2)

    board.play()
    # player_1_first_moves = [
    #     [
    #         ((0,5),16)
    #     ],
    #     [
    #         ((7,5),17)
    #     ]
    
    # ]

    # player_1 = HumanPlayer("Player 1", 1, pre_moves=player_1_first_moves)



    # player_2_first_moves = [
    #     [
    #         ((9,5),16)
    #     ],
    #     [
    #         ((6,5),5),
    #         ((7,6),5),
    #         ((7,4),5),
    #         ((8,5),2)
    #     ]
    
    # ]

    # player_2 = HumanPlayer("Player 2", -1, pre_moves=player_2_first_moves)
