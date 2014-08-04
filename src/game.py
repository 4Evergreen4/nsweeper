import curses
import time
from interface.window import popup
import board

def game(screen, main_w, main_h, field_w, field_h, mine_num):
    #popup(0,0,5,1, 'nsweeper', 'a popup testing zone', screen)
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
    mainwin = curses.newwin(main_h+2, main_w+2, 0, 0)

    cursor_x = 1
    cursor_y = 1

    while True:
        key = screen.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP:
            mainwin.addch(cursor_y, cursor_x, ' ')
            cursor_y -= 1
        if key == curses.KEY_DOWN:
            mainwin.addch(cursor_y, cursor_x, ' ')
            cursor_y += 1
        if key == curses.KEY_LEFT:
            mainwin.addch(cursor_y, cursor_x, ' ')
            cursor_x -= 1
        if key == curses.KEY_RIGHT:
            mainwin.addch(cursor_y, cursor_x, ' ')
            cursor_x += 1

        if cursor_y < 1:
            cursor_y = 1
        elif cursor_y > main_h:
            cursor_y = main_h

        if cursor_x < 1:
            cursor_x = 1
        elif cursor_x > main_w:
            cursor_x = main_w

        mainwin.addch(cursor_y, cursor_x, ' ', curses.A_STANDOUT)
        mainwin.border()
        mainwin.refresh()
