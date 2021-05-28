""" Visualizer module """

import algorithms
import time
import os
import sys
import pygame as pg

# Window length and breadth.
# Breadth should be equal to the size of the array.
DIMENSIONS = (1024, 512)

# Map algorithms to the classes from algorithms.py
ALGORITHMS = {
    "SelectionSort": algorithms.SelectionSort(),
    "BubbleSort": algorithms.BubbleSort(),
    "InsertionSort": algorithms.InsertionSort(),
    "MergeSort": algorithms.MergeSort(),
    "QuickSort": algorithms.QuickSort()
}

# Set canvas dimensions.
display = pg.display.set_mode(DIMENSIONS)
# Fill the window with color.
display.fill(pg.Color("#a48be0"))


def check_events():
    # Looks for when the pg window has been quit.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


def update(algorithm, swap1=None, swap2=None, display=display):
    # Function that draws the sorted array on each iteration.
    display.fill(pg.Color("#a48be0"))
    # To be displayed on title bar.
    pg.display.set_caption(
        f"Sorting Visualizer | Algorithm: {algorithm.name} | Time: {time.time() - algorithm.start_time:.3f}"
    )
    k = int(DIMENSIONS[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        color = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            print(algorithm.array[i])
            color = (0, 255, 0)
        elif swap2 == algorithm.array[i]:
            color = (255, 0, 0)
            print(algorithm.array[i])
        pg.draw.rect(
            display, color, (i*k,DIMENSIONS[1],k,-algorithm.array[i])
        )
    check_events()
    pg.display.update()


def keep_open(algorithm, display, time):
    # Keep window open until sort completion.
    pg.display.set_caption(
        f"Sorting Visualizer | Algorithm: {algorithm.name}  | Time: {time:.3f} | Status: Done!")
    while True:
        check_events()


def main(args):
    if len(sys.argv) < 2:
        print("Select a sorting algorithm.")
    elif args[1] == "list":
        print(f"Available algorithms: {', '.join(ALGORITHMS.keys())}")
        sys.exit(0)
    else:
        try:
            algorithm = ALGORITHMS[args[1]]
            _, time_elapsed = algorithm.run()
            keep_open(algorithm, display, time_elapsed)
        except Exception as e:
            print(f"Something's wrong: {e}")


if __name__ == "__main__":
    main(sys.argv)
