from .Core import Controller
import controller.State as State

class ClientController(Controller):
    def __init__(self, url = None):
        super().__init__(url)
        self.AddState("Normal", State.NormalState(self, self._model))
        self.AddState("Insert", State.InsertState(self, self._model))
        self.AddState("Search", State.SearchState(self, self._model))
        self.AddState("Command", State.CommandState(self, self._model))
        self.ChangeState("Normal")

    def draw(self):
        self._view.draw(self._model.getString(), self._model.getPosCursor())