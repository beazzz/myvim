import curses
from view.View import View
from model.Data import Data


class Controller():
    def __init__(self,):
        self.__canvas = curses.initscr()
        self.__view = View(self.__canvas)
        self.__model = Data()
        self.__commandName = ""
        self.__argsForCommand = None 


    def execute(self):
        c = self.__canvas.getkey()
        
    def __draw():
        pass



        
    



      

    
