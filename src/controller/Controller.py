import curses
from view.View import View
from model.Data import Data


class Controller():
    def __init__(self):
        self.view = View()
        self.model = Data()

    def execute(self, commandName):
        self.model.handleInput(commandName)

        
    



      

    
