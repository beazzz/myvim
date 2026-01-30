from model.Model import Model
from view.View import View
from .Commands import Command

class Controller():
    def __init__(self):
        self.__view = View()
        self.__model = Model(self.__view)
        self.__commands = []

    def InitCommand(self, command):
        self.__commands.append(command)
        
    



      

    
