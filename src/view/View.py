import curses
from MyString import MyString as MyString

class View():
    def __init__(self):
        self.__canvas = curses.initscr()
        self.__canvas.keypad(True)
        curses.noecho()
        #self.__canvas.scrollok(False)

    def endwin(self):
        curses.endwin()

    def getkey(self):
        return self.__canvas.getkey()

    def draw(self, strings : list[str], cursorPos : dict):
        self.__canvas.clear()

        y = 0
        for string in strings:
            y_win, x_win = self.__canvas.getmaxyx()
            if (y >= y_win):
                break
            self.__canvas.addstr(y, 0, string)
            y += 1

        self.__canvas.move(cursorPos['y'], cursorPos['x'])
        self.__canvas.refresh()