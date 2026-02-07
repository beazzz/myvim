import curses

class View():
    def __init__(self, canvas : curses):
        # print("Create View", self)
        self.__canvas = canvas