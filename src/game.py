import curses
import curses.panel
import cursor
import time
import interface.window
import board

def game(stdscr, screen, screen_panel, edge, edge_panel, field_h, field_w, mine_num):
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
    
    key = 0
    done = False
    while not(done):
        if key == ord('q'):
            return 'menu'
        stdscr.refresh()
        edge_panel.bottom()
        edge.border()
        edge.refresh()
        screen.addstr(0, 1, 'Nothing here yet.  Press q to exit to menu')
        screen_panel.top()
        screen.refresh()
        key = stdscr.getch()
