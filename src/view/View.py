import curses
from MyString import MyString as MyString

class View():
    def __init__(self, canvas : curses):
        # print("Create View", self)
        self.__canvas = canvas

    def draw(self, strings : list):
        # print(string)
        i = 0
        for string in strings:
            self.__canvas.addstr(i, 0, string.c_str())
            i += 1
            
        self.__canvas.refresh()
        curses.napms(3000)