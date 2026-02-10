from .Core import Controller
import controller.State as State
import curses

class ClientController(Controller):
    def __init__(self, url = None):
        super().__init__(url)
        self.AddState("Normal", State.NormalState(self, self._model))
        self.AddState("Insert", State.InsertState(self, self._model))
        self.AddState("Search", State.SearchState(self, self._model))
        self.AddState("Command", State.CommandState(self, self._model))
        self.ChangeState("Normal")

    def draw(self):
        self._model.draw()

    def showHelp(self):
        strings = []
        print("showHelp")
        for key in self._states:
            strings.append("__________________"+key+"__________________")
            # for command in self._states[key].getCommands():
            #     strings.append(command)

        posCursor = {'x': 0, 'y':0}
        self._view.draw(strings, posCursor)
        self._view.getkey()

    def execute(self):
        ch = self._view.getkey()
        self.handleInput(ch)

    def close(self) -> bool:
        status = self._model.close()
        return status
        