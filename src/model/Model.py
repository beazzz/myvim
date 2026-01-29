import sys
from view.View import View
from MyString import MyString


class Model:
    def __init__(self):
        # contructor
        self.view = View()
        self.string = MyString()
        self.mode = 0
        self.index = 0

    def open(self):
        pass

    def close(self):
        pass

    def update(self):
        self.view.draw()

    def commandA(self):
        pass


    # Setters
    def SetView(self,  view):
        self.view = view
        
    def SetMode(self, mode):
        self.mode = mode

    def SetIndex(self, index):
        self.index = index
    
    # Getters
    def GetMode(self):
        return self.mode
    def GetIndex(self):
        return self.index