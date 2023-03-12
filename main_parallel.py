import random
import multiprocessing
import sys
import time


def run_guardian():
    guardian = Guardian()
    guardian.run()

if __name__ == '__main__':

    guardian_proc = multiprocessing.Process(target=run_guardian(), args=(f'{i}',))


    processes = []
    for i in range(6):
        process = multiprocessing.Process(target=run, args=(f'{i}',))
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()
