import curses
from view.View import View
from model.Data import Data


class Controller:
    def __init__(self):
        self._canvas = curses.initscr()
        self._view = View(self.__canvas)
        self._state = State(self)
        self._states = {}
        self._commandName = ""

    def ChangeState(self, stateName : str):
        state = self.__states.get(stateName)
        if state is None:
            print("State is incorrect")
            return
        self.__state = state

    def AddState(self, stateName: str, state : 'State'):
        self.__states[stateName] = state

    def handleInput(self, commandName : str, *args):
        return self.__state.handleInput(commandName, *args)

    def execute(self):
        c = self.__canvas.getkey()
        
    def _draw():
        pass

class Command:
    """
    Parent for OtherCommands
    """
    def __init__(self, editor: Data):
        self._editor = editor

    def execute(self, *args) -> bool:
        return False
    
class State:
    """
    Parent for OtherState
    For Command is Invoker
    """
    def __init__(self, context : Controller):
        #print("Create State", self)
        self._commands: dict[Command] = {}
        self._context = context
    
    def handleInput(self, commandName : str, *args)-> bool:
        """
        Pass control to Command
        """
        #print("State handle command", commandName, self)
        command = self._commands.get(commandName, "Error command")
        return command.execute(*args)
        
    def addCommmand(self, commandName : str, command: Command):
        #print("State add command", commandName, self)
        self._commands[commandName] = command
        
    def ChangeState(self, stateName : str):
        # print("State change state", stateName, self)
        self._context.ChangeState(stateName)



        
    



      

    
