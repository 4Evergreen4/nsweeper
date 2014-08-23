import curses
import curses.panel
import interface.window
import board

def game(stdscr, screen, screen_panel, field_h, field_w, mine_num):
    minefield = board.newboard(field_h, field_w, mine_num)
    minefield_list = minefield.getlist()
    display = draw(minefield, 1, 2)
    screen.clear()

    key = 0
    done = False
    while not(done):
        if key == ord('q'):
            return 'menu'
        display.cursormove(key)
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
        self.boardh = len(self.blist)
        self.boardw = len(self.blist[0])
        self.cursorx = 0
        self.cursory = 0
        self.field = curses.newwin(self.boardh + 2,
                                   (self.boardw * 2) + 3, y, x)
        self.fieldp = curses.panel.new_panel(self.field)

    def drawboard(self):
        self.field.border()
        for h in range(0, len(self.blist)):
            i = 0
            for w in range(0, len(self.blist[h])):
                i += 1
                if h == self.cursory and w == self.cursorx:
                    self.field.addch(h + 1, (w + 1) + i,
                                     self.blist[h][w], curses.A_STANDOUT)
                else:
                    self.field.addch(h + 1, (w + 1) + i, self.blist[h][w])
        self.fieldp.top()
        self.field.refresh()

    def setcursorpos(self, y, x):
        self.cursorx = x
        self.cursory = y

    def getcursorpos(self):
        return self.cursory, self.cursorx

    def cursormove(self, key):
        if key == curses.KEY_UP:
            self.cursory -= 1
        if key == curses.KEY_DOWN:
            self.cursory += 1
        if key == curses.KEY_RIGHT:
            self.cursorx +=1
        if key == curses.KEY_LEFT:
            self.cursorx -= 1

        if self.cursorx > self.boardw - 1:
            self.cursorx = self.boardw - 1
        elif self.cursorx < 0:
            self.cursorx = 0

        if self.cursory > self.boardh - 1:
            self.cursory = self.boardh - 1
        elif self.cursory < 0:
            self.cursory = 0
