import curses
import curses.panel
import cursor
import time
import interface.window
import board

def game(stdscr, screen, screen_panel, edge, edge_panel, field_h, field_w, mine_num):
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
    return 'menu'
