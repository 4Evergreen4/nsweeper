import curses
import time
from interface.window import popup
import board

def game(screen, field_w, field_h, mine_num):
    #popup(0,0,5,1, 'nsweeper', 'a popup testing zone', screen)
    minefield = board.newboard(field_h, field_w)
    display = curses.newwin(field_h+2, field_w+2, 0, 0)
    minefield_list = minefield.getlist()
    for y in range(0, len(minefield_list)):
        for x in range(0, len(minefield_list[y])):
            display.addstr(y+1,x+1,str(minefield_list[y][x]))
    display.border()
    display.refresh()
    time.sleep(3)
