import curses

class newboard(object):
    def __init__(self, w, h, x, y):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.array = []

        for height in range(0, self.h):
            self.array.append([])
            for width in range(0, self.w):
                self.array[height].append('')

    def getitem(self, x, y):
        return self.array[y][x]

    def display(self, screen):
        for h in range(0, len(self.array)):
            screen.addstr(self.y + h, self.x, str(self.array[h]))
        screen.refresh()

        #for height in self.array:
        #    print height
