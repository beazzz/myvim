import curses
from MyString import MyString as MyString

class View():
    def __init__(self):
        self.__canvas = curses.initscr()
        self.__canvas.keypad(True)
        curses.noecho()

    def getMaxXY(self):
        return self.__canvas.getmaxyx()

    def endwin(self):
        curses.endwin()

    def getkey(self):
        return self.__canvas.getkey()
    
    def moveCursor(self, cursorPos : dict):
        self.__canvas.move(cursorPos['y'], cursorPos['x'])

    def clear(self):
        self.__canvas.clear()
    
    def refresh(self):
        self.__canvas.refresh()

    def draw(self, strings : list[str], tempPos, modeNum):
        
        y_max, x_max = self.getMaxXY()
        y_max -= 2
        x_max -= 1

        y_cur, x_cur = tempPos['y'], tempPos['x']

        y_min = y_cur - y_max
        x_min = x_cur - x_max
        if y_min < 0: y_min = 0
        if x_min < 0: x_min = 0

        strings = strings[y_min:y_min+y_max+1]
        for i in range(len(strings)):
            strings[i] = strings[i][x_min:x_min+x_max+1]

        nums = 0
        if modeNum:
            nums = len(str(len(strings))) # Size number
            for i, string in enumerate(strings):
                num = str(i+y_min)
                num += ' '* (nums-len(num)) # Add space to make perfect nums
                self.__canvas.addstr(i, 0, num + " | " + string)
            nums = len(str(nums) + " | ") + 1
        else:
            for i, string in enumerate(strings):
                self.__canvas.addstr(i, 0, string)
        
        tempPos['x'] -= x_min - nums
        tempPos['y'] -= y_min
        self.moveCursor(tempPos)

    def drawStringInPos(self, y, x, string):
        """
        Docstring for drawStringInPos
        
        :param y: column
        :param x: raw
        :param string: string
        """
        y_cur,x_cur = self.__canvas.getyx()
        self.__canvas.addstr(y, x, string)
        self.__canvas.move(y_cur, x_cur)