import curses

def popup(x, y, w, h, title, text, screen):

    topstr = str(title) + "-" * ((len(text) - len(title)) + 2)

    screen.addstr(y, x, str(topstr))

    midstr = "|" + text + "|"

    screen.addstr(y + 1, x, str(midstr))

    endstr = "-" * (len(text) + 2)

    screen.addstr(y + 2, x, str(endstr))

    screen.refresh()

class button(object):
    def __init__(self, x, y, text):
        self.text = text
        self.x = x
        self.y = y

    def getstate():
        pass
