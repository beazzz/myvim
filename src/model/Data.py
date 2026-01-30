from view.View import View
from .State import State
from MyString import MyString


class Data:
    def __init__(self, view: View, state : State):
        # contructor
        self.view = view
        self.string = MyString()
        self.state = state

    # command with files      
    def open(self):
        pass
    def close(self):
        pass

    # command with views
    def update(self):
        self.view.draw()

    # command with text
    def delete(self):
        pass
    def cut(self):
        pass
    def copy(self):
        pass
    def put(self):
        pass