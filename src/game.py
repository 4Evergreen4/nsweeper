import curses
import time
from interface.window import popup
import board

def game(screen, win_x, win_y, win_w, win_h):
    #popup(0,0,5,1, 'nsweeper', 'a popup testing zone', screen)
    win = curses.newwin(win_h, win_w, win_y, win_x)
    sweep = board.newboard(5, 5)
    sweep.display(0, 0, win)
    time.sleep(2)
