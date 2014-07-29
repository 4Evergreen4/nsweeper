import curses
import time
from interface.window import popup

def game(screen, win_x, win_y, win_w, win_h):
    popup(0,0,5,1, 'nsweeper', 'a popup testing zone', screen)
    time.sleep(2)
