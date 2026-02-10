import curses
from MyString import MyString as MyString

class View():
    def __init__(self, canvas : curses):
        # print("Create View", self)
        self.__canvas = canvas
        self.__canvas.scrollok(True)

    def draw(self, strings : list[str], cursorPos):
        self.__canvas.clear()

        y = 0
        for string in strings:
            y_win, x_win = self.__canvas.getmaxyx()
            # if (y >= y_win):
            #     break
            self.__canvas.addstr(string + '\n')
            y += 1

        self.__canvas.scroll()
        self.__canvas.move(cursorPos['y'], cursorPos['x'])
        self.__canvas.refresh()