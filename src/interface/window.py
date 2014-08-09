import curses

buttons = []

def popup(x, y, w, h, title, text, screen):

    topstr = str(title) + "-" * ((len(text) - len(title)) + 2)

    screen.addstr(y, x, topstr)

    midstr = "|" + text + "|"

    screen.addstr(y + 1, x, midstr)

    endstr = "-" * (len(text) + 2)

    screen.addstr(y + 2, x, endstr)

    screen.refresh()

def buttonhandler(first, key, *btns): # btns = buttons
    cur_button = first



class newbutton(object):
    def __init__(self, x, y, text, cyclenum):
        self.text = text
        buttons.append(text)
        self.x = x
        self.y = y
        self.cyclenum = cyclenum

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
