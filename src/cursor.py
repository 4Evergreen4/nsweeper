import curses
class newcursor(object):
    def __init__(self, startx, starty, main_h, main_w):
        self.cursor_x = startx
        self.cursor_y = starty
        self.main_h = main_h
        self.main_w = main_w

    def update(self, key, screen):
        if key == curses.KEY_UP:
            screen.addch(self.cursor_y, self.cursor_x, ' ')
            self.cursor_y -= 1
        if key == curses.KEY_DOWN:
            screen.addch(self.cursor_y, self.cursor_x, ' ')
            self.cursor_y += 1
        if key == curses.KEY_LEFT:
            screen.addch(self.cursor_y, self.cursor_x, ' ')
            self.cursor_x -= 1
        if key == curses.KEY_RIGHT:
            screen.addch(self.cursor_y, self.cursor_x, ' ')
            self.cursor_x += 1

        if self.cursor_y < 0:
            self.cursor_y = 0
        elif self.cursor_y > self.main_h - 1:
            self.cursor_y = self.main_h - 1

        if self.cursor_x < 0:
            self.cursor_x = 0
        elif self.cursor_x > self.main_w - 1:
            self.cursor_x = self.main_w - 1

    def display(self, screen):
        screen.addch(self.cursor_y, self.cursor_x, '#', curses.A_STANDOUT)
