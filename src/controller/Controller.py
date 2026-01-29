from model.Model import Model
from view.View import View
from .Commands import Command

class Controller():
    def __init__(self):
        self.model = Model()
        self.commands = Command(self.model)
        self.view = View()

    
