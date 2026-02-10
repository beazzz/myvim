import curses
from MyString import MyString as MyString

class View():
    def __init__(self):
        self.__canvas = curses.initscr()
        self.__canvas.keypad(True)
        curses.noecho()
        #self.__canvas.scrollok(False)

    def getMaxXY(self):
        return self.__canvas.getmaxyx()

    def endwin(self):
        curses.endwin()

    def getkey(self):
        return self.__canvas.getkey()
    
    def moveCursor(self, cursorPos : dict):
        self.__canvas.move(cursorPos['y'], cursorPos['x'])

    def draw(self, strings : list[str]):
        self.__canvas.clear()

        for string in strings:
            self.__canvas.addstr(string + '\n')
        
        self.__canvas.refresh()