import curses
import game

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
    stdscr.nodelay(1)

    game.game(stdscr, main_w, main_h, field_w, field_h, mine_num)

    stop(stdscr)

def stop(stdscr):
    # Reset everything
    stdscr.keypad(0)
    stdscr.nodelay(0)
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()
