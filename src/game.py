import curses
import time

def game(screen):
    # Sets the starting coordinates
    win_x = 0
    win_y = 0
    # Sets the curses window size
    win_w = 80
    win_h = 24
    
    win = curses.newwin(win_h, win_w, win_y, win_x)
    win.refresh()
    
    time.sleep(2)
