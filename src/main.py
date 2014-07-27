import curses
import game

def main():
    '''Start game'''

    # Starts ncurses
    stdscr = curses.initscr()
    
    term_size = stdscr.getmaxyx()
    
    if term_size[0] < 24 or term_size[1] < 80:
        curses.endwin()
        print "ERROR: Your console screen is smaller than 80x24."
        print "Please resize your window and try again."
        return 1;
    
    # Setup ncurses
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    stdscr.nodelay(1)
    
    game.game(stdscr)
    
    stop(stdscr)

def stop(stdscr):
    # Reset everything
    stdscr.keypad(0)
    stdscr.nodelay(0)
    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()
