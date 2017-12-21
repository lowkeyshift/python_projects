#!/bin/python3
import os

import pyautogui as pyg


def clear():
    """Clear command that will clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def mouse_locate():
    """Return current position mouse pointer; returns the x,y."""
    try:
        while True:
            m_position = pyg.position()
            print(chr(27) + "[2J")
            print(m_position)
    except KeyboardInterrupt:
        print('Interrupted by user!')


mouse_locate()
