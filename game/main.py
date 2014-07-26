import curses

def main():
    '''Start game'''

    # Starts ncurses
    stdscr = curses.initscr()

    # Setup ncurses
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    stdscr.nodelay(1)

    # Reset everything
    stdscr.keypad(0)
    stdscr.nodelay(0)
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()
