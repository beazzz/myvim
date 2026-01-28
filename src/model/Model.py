import sys
from view.View import View
from MyString import MyString


class Model:
    def __init__(self):
        # contructor
        self.view = View()
        self.string = MyString()
        self.mode = 0

    def open(self):
        pass

    def close(self):
        pass

    def update(self):
        pass

    def commandA(self):
        pass