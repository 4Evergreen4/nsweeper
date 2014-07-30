import curses
import game

def main():
    '''Start game'''

    # Sets the starting coordinates
    win_x = 0
    win_y = 0
    # Sets the curses window size
    win_w = 80
    win_h = 24

    # Starts ncurses
    stdscr = curses.initscr()

    term_size = stdscr.getmaxyx()

    if term_size[0] < 24 or term_size[1] < 80:
        curses.endwin()
        print "ERROR: Your console screen is smaller than 80x24."
        print "Please resize your window and try again."
        return 1

    # Setup ncurses
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    stdscr.nodelay(1)

    game.game(stdscr, win_x, win_y, win_w, win_h)

    stop(stdscr)

def stop(stdscr):
    # Reset everything
    stdscr.keypad(0)
    stdscr.nodelay(0)
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()
