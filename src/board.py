import curses

class newboard(object):
    '''Creates a 2d array.'''
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.array = []

        for height in range(0, self.h):
            self.array.append([])
            for width in range(0, self.w):
                self.array[height].append('')

    def getitem(self, x, y):
        '''Returns value from the 2d array'''
        return self.array[y][x]

    def setitem(self, x, y, item):
        '''Sets an item in the 2d array.'''
        self.array[y][x] = item

    def display(self, x, y, screen=0):
        '''Displays the 2d array.'''
        if screen != 0:
            for h in range(0, len(self.array)):
                screen.addstr(y + h, x, str(self.array[h]))
            screen.refresh()
        else:
            for height in self.array:
                print height
