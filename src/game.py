import curses
import curses.panel
import cursor
import time
from interface.window import popup
import board

def game(screen, main_w, main_h, field_w, field_h, mine_num):
    #popup(0,0,5,1, 'nsweeper', 'a popup testing zone', screen)
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
    edge = curses.newwin(main_h+2, main_w+2, 0, 0)
    edge_panel = curses.panel.new_panel(edge)
    display = curses.newwin(main_h, main_w, 1, 1)
    display_panel = curses.panel.new_panel(display)
    cursor_x = 0
    cursor_y = 0
    selector = cursor.newcursor(cursor_y,cursor_x,main_h,main_w)

    while True:
        key = screen.getch()
        if key == ord('q'):
            break

        edge.border()
        edge_panel.bottom()
        edge.refresh()
        selector.update(key, display)
        selector.display(display)
        display_panel.top()
        display.refresh()
        time.sleep(0.01)
