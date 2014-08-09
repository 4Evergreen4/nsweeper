import curses
import curses.panel
import cursor
import time
import interface.window
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
    cur_button = 0
    selector = cursor.newcursor(cursor_x, cursor_y, main_h, main_w)
    play = interface.window.newbutton(40, 16, 'play', 0)
    play.setstate(True)
    quit = interface.window.newbutton(40, 10, 'quit', 1)
    quit.setstate(False)

    while True:
        key = screen.getch()
        if key == ord('q'):
            break

        edge.border()
        edge_panel.bottom()
        edge.refresh()
        play.display(display, 20, 5)
        quit.display(display, 20, 8)
        if quit.getstate() == True and key == 32:
            break
        if key == curses.KEY_UP and cur_button == 1:
            cur_button -= 1
            play.setstate(True)
            quit.setstate(False)
        elif key == curses.KEY_DOWN and cur_button == 0:
            cur_button += 1
            play.setstate(False)
            quit.setstate(True)
        
        display_panel.top()
        display.refresh()
        time.sleep(0.01)
