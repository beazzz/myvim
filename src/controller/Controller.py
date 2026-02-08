from .Core import Controller
import controller.State as State

class ClientController(Controller):
    def __init__(self):
        super().__init__()
        self.AddState("Normal", State.NormalState)
        self.AddState("Insert", State.InsertState)
        self.AddState("Search", State.SearchState)
        self.AddState("Command", State.CommandState)
        self.ChangeState("Normal")      

    def draw(self):
        pass