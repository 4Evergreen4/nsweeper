import curses
import curses.panel
import interface.window
import board

def game(stdscr, screen, screen_panel, field_h, field_w, mine_num):
    minefield = board.newboard(field_h, field_w)
    minefield_list = minefield.getlist()
    display = draw(minefield, 1, 2)
    screen.clear()

    key = 0
    done = False
    while not(done):
        if key == ord('q'):
            return 'menu'
        stdscr.refresh()
        screen.border()
        screen_panel.bottom()
        screen.refresh()
        display.drawboard()
        key = stdscr.getch()

class draw(object):
    def __init__(self, board, y, x):
        self.board = board
        self.blist = self.board.getlist()
        self.y = y
        self.x = x
        self.field = curses.newwin(len(self.blist) + 2,
                                   (len(self.blist[0]) * 2) + 3, y, x)
        self.fieldp = curses.panel.new_panel(self.field)

    def drawboard(self):
        self.field.border()
        for h in range(0, len(self.blist)):
            i = 0
            for w in range(0, len(self.blist[h])):
                i += 1
                self.field.addch(h + 1, (w + 1) + i, self.blist[h][w])
        self.fieldp.top()
        self.field.refresh()
