#!/bin/python3
import pyautogui as pyg


def mouse_locate():
    """Return current position mouse pointer; returns the x,y."""
    print("Press Crtl-C to quit mouse tracker.")
    try:
        while True:
            x, y = pyg.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\nInterrupted by user!')


mouse_locate()
