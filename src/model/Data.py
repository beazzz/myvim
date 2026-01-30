from view.View import View
from .State import State
from .Command import Command
from MyString import MyString


class Data:
    def __init__(self, view: View, state : State):
        # contructor
        self.__view = view
        self.__string = MyString()
        self.__state = state

    def handleInput(self, command: Command):
        self.__state.handleInput(command)

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