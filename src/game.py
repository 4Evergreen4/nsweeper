import curses
import time

def game(screen, win_x, win_y, win_w, win_h):
    win = curses.newwin(win_h, win_w, win_y, win_x)
    win.refresh()
    
    time.sleep(2)
