import curses
import curses.panel
import cursor
import time
import interface.window
import board

def game(screen, main_w, main_h, field_w, field_h, mine_num):
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
    edge = curses.newwin(main_h+2, main_w+2, 0, 0)
    edge_panel = curses.panel.new_panel(edge)
    display = curses.newwin(main_h, main_w, 1, 1)
    display_panel = curses.panel.new_panel(display)
    cursor_x = 0
    cursor_y = 0
    selector = cursor.newcursor(cursor_x, cursor_y, main_h, main_w)
    play = interface.window.newbutton(40, 16, 'play', 0)
    quit = interface.window.newbutton(40, 10, 'quit', 1)
    button_handler = interface.window.newbuttonhandler(0, play, quit)

    done = False
    while not(done):
        key = screen.getch()
        if key == ord('q'):
            done = True

        edge.border()
        edge_panel.bottom()
        edge.refresh()
        play.display(display, 20, 5)
        quit.display(display, 20, 8)
        if quit.getstate() == True and key == 32:
            done = True

        button_handler.update(key)

        display_panel.top()
        display.refresh()
        time.sleep(0.01)
