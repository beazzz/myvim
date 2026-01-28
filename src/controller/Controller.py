from model.Model import Model
from view.View import View


class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()
        pass