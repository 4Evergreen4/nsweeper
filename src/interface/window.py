import curses

buttons = []

def popup(x, y, title, text, screen):

    topstr = str(title) + "-" * ((len(text) - len(title)) + 2)

    screen.addstr(y, x, topstr)

    midstr = "|" + text + "|"

    screen.addstr(y + 1, x, midstr)

    endstr = "-" * (len(text) + 2)

    screen.addstr(y + 2, x, endstr)

    screen.refresh()

class newbuttonhandler(object):
    def __init__(self, first, *btns): # btns = buttons
        self.cur_button = first
        self.btns = btns

    def update(self, key):
        if key == curses.KEY_UP and self.cur_button > 0:
            self.cur_button -= 1
        if key == curses.KEY_DOWN and self.cur_button < len(self.btns) - 1:
            self.cur_button += 1

        self.btns[self.cur_button - 1].setstate(False)
        self.btns[self.cur_button].setstate(True)


class newbutton(object):
    def __init__(self, x, y, text, cyclenum):
        self.text = text
        buttons.append(text)
        self.x = x
        self.y = y
        self.cyclenum = cyclenum
        self.state = False

    def getcyclenum(self):
        return self.cyclenum

    def getstate(self):
        return self.state

    def setstate(self, state):
        self.state = state

    def display(self, screen, x, y):
        if self.state == True:
            top = "-" * (len(self.text) + 2)
            screen.addstr(y, x, top)
            screen.addstr(y + 1, x, "|")
            screen.addstr(y + 1, x + 1, self.text, curses.A_STANDOUT)
            screen.addstr(y + 1, x + (len(self.text) + 1), "|")
            screen.addstr(y + 2, x, top)
        else:
            top = "-" * (len(self.text) + 2)
            screen.addstr(y, x, top)
            mid = "|" + self.text + "|"
            screen.addstr(y + 1, x, mid)
            screen.addstr(y + 2, x, top)
