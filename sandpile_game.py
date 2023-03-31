from GameBoard import GameBoard
from HumanPlayer import HumanPlayer
from RandomFirstRowPlayer import RandomFirstRowPlayer
from threading import Event


import cv2
import threading
import queue
import time


def start_game(frame_queue):
    player_1 = RandomFirstRowPlayer("Player 1", 1, 0)
    player_2 = RandomFirstRowPlayer("Player 2", -1, 127)
    
    board = GameBoard(player_1, player_2, frame_queue=frame_queue)

    board.play()



if __name__ == '__main__':
    
    # Define the frame size and frame rate
    s_width = 1920
    s_height = 1080
    fps = 60
    
    # Create a queue to hold the frames
    frame_queue = queue.Queue()

    # Start the frame generation thread
    s_thread = threading.Thread(target=start_game, args=([frame_queue]))
    s_thread.daemon = True
    s_thread.start()

    length = 0

    # Create the video stream writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(f"output-{length}.mp4", fourcc, fps, (s_width, s_height))


    # Loop over the frames in the queue
    while True:
        # Get the next frame from the queue
        try:
            image = frame_queue.get_nowait()
        except queue.Empty:
            time.sleep(3)
            continue

        out.write(image)
        length += 1
        print(length)

        if length % 3600 == 0 :
            # Release the video stream writer and close the display window
            out.release()
            out = cv2.VideoWriter(f"output-{length}.mp4", fourcc, fps, (s_width, s_height))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
