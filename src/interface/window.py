import curses

def popup(x, y, w, h, title, text, screen):

    topstr = str(title) + "-" * ((len(text) - len(title)) + 2)

    screen.addstr(y, x, topstr)

    midstr = "|" + text + "|"

    screen.addstr(y + 1, x, midstr)

    endstr = "-" * (len(text) + 2)

    screen.addstr(y + 2, x, endstr)

    screen.refresh()

class button(object):
    def __init__(self, x, y, text):
        self.text = text
        self.x = x
        self.y = y

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
