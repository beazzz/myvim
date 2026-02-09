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

        self._canvas.keypad(True)

    def draw(self):
        # print(self._model.getPosCursor())
        strings = [string.c_str() for string in self._model.getString()]
        self._view.draw(strings, self._model.getPosCursor())

    def showHelp(self):
        strings = []
        print("showHelp")
        for key in self._states:
            # print("__________________",key,"__________________")
            strings.append("__________________"+key+"__________________")
            # for command in self._states[key].getCommands():
            #     strings.append(command)

        posCursor = {'x': 0, 'y':0}
        self._view.draw(strings, posCursor)
        self._canvas.getkey()

    def execute(self):
        ch = self._canvas.getkey()
        self.handleInput(ch)