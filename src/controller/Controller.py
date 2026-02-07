import curses
from view.View import View
from model.Data import Data


class Controller():
    def __init__(self, model : Data = Data(), view : View = View()):
        self.__view = view
        self.__model = model
        self.__canvas = curses.initscr()
        self.__commandName = ""

    def execute(self, commandName, *args):
        self.__commandName += commandName
        if self.__model.handleInput(commandName, args):
            self.__commandName = ""

    def __draw():
        pass

        
    



      

    
