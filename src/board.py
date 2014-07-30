import curses

class board(object):
    def __init__(self, w, h, x, y, screen):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.screen = screen
        self.array = []

        for height in range(0, self.h):
            self.array.append([])
            for width in range(0, self.w):
                self.array[height].append('')

    def getitem(self, x, y):
        return self.array[y][x]
