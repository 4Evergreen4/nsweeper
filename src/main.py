import curses
import statehandler

def main():
    '''Start game'''

    #
    # Config Stuff
    #

    # Size of main window
    main_h = 24
    main_w = 80
    # Size of minefield
    field_h = 8
    field_w = 8
    # Number of mines
    mine_num = 10

    #
    # Game initialization
    #

    # Starts ncurses
    stdscr = curses.initscr()

    term_size = stdscr.getmaxyx()

    if term_size[0] < main_h+2 or term_size[1] < main_w+2:
        curses.endwin()
        print "ERROR: Your console screen is smaller than %sx%s." % (
              main_w+2, main_h+2)
        print "Please resize your window and try again."
        return 1

    # Setup ncurses
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)

    try:
        display = curses.newwin(main_h, main_w, 0, 0)
        display_panel = curses.panel.new_panel(display)
        statehandler.statehandler(
            stdscr, display, display_panel, field_h, field_w, mine_num
        )
        stop(stdscr)
    except Exception:
        stop(stdscr)
        raise
        return 1;

def stop(stdscr):
    # Reset everything
    stdscr.keypad(0)
    stdscr.nodelay(0)
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()
