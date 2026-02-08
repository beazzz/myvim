import curses
from view.View import View
from model.Data import Data


class Controller:
    def __init__(self, url = None):
        self._canvas = curses.initscr()
        self._view = View(self._canvas)
        self._model = Data(self._view, url)
        self._state = State(self, self._model)
        self._states = {}

    def ChangeState(self, stateName : str):
        state = self._states.get(stateName)
        if state is None:
            print("State is incorrect")
            return
        self._state = state
        # print("ChangeState:", stateName, self)

    def AddState(self, stateName: str, state : 'State'):
        # print("AddState:", stateName, self)
        self._states[stateName] = state

    def handleInput(self, ch : str):
        # print("handleInput", ch, self)
        return self._state.handleInput(ch)

    def execute(self):
        pass
        
    def _draw():
        pass

class Command:
    """
    Parent for OtherCommands
    """
    def __init__(self, editor: Data):
        self._editor = editor

    def execute(self, *args) -> bool:
        # print("Command: ", self)
        return False
    
class State:
    """
    Parent for OtherState
    For Command is Invoker
    """
    def __init__(self, context : Controller, model: Data):
        #print("Create State", self)
        self._commands: dict[Command] = {}
        self._context = context
        self._model = model
    
    def handleInput(self, ch : str)-> bool:
        """
        Pass control to Command
        """
        return False
        
    def addCommand(self, commandName : str, command: Command):
        # print("State add command", commandName, self)
        self._commands[commandName] = command
        
    def ChangeState(self, stateName : str):
        self._context.ChangeState(stateName)



        
    



      

    
