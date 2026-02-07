import curses
from view.View import View
from model.Data import Data


class Controller():
    def __init__(self, model : Data = None):
        self.view = View()
        self.model = model

    def execute(self, commandName):
        self.model.handleInput(commandName)

        
    



      

    
