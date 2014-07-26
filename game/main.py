import curses

def main():
    '''Start game'''

    # Starts ncurses
    stdscr = curses.initscr()

    # Setup ncurses
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    # Reset everything
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()
