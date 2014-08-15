import curses
import curses.panel
import cursor
import time
import interface.window
import board

def game(stdscr, screen, main_w, main_h, field_w, field_h, mine_num):
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
