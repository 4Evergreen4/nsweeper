import curses
import curses.panel
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

    while True:
        display.addch(cursor_y, cursor_x, ' ', curses.A_STANDOUT)
        key = screen.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP:
            cursor_y -= 1
        if key == curses.KEY_DOWN:
            cursor_y += 1
        if key == curses.KEY_LEFT:
            cursor_x -= 1
        if key == curses.KEY_RIGHT:
            cursor_x += 1

        if cursor_y < 0:
            cursor_y = 0
        elif cursor_y > main_h - 1:
            cursor_y = main_h - 1

        if cursor_x < 0:
            cursor_x = 0
        elif cursor_x > main_w - 1:
            cursor_x = main_w - 1

        edge.border()
        edge_panel.bottom()
        edge.refresh()
        display_panel.top()
        display.refresh()
        time.sleep(0.01)
