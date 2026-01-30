from view.View import View
from .State import State
from MyString import MyString


class Data:
    def __init__(self, view: View):
        # contructor
        self.__posCursor = {'x': 0,
                            'y': 0
        }
        self.__view = view 
        self.__string = MyString()
        self.__state : list[State] = []

    def handleInput(self, commandName):
        self.__state.handleInput(commandName)

    # command with files      
    def open(self):
        pass
    def close(self):
        pass

    # command with views
    def update(self):
        self.__view.draw()

    # command with text
    def delete(self):
        pass
    def cut(self):
        pass
    def copy(self):
        pass
    def put(self):
        pass

    def posCursor(self, coord, value):
        self.__posCursor[coord]+= value
