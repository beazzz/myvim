import curses
from view.View import View
from model.Data import Data


class Controller():
    def __init__(self,):
        self.__canvas = curses.initscr()
        self.__view = View(self.__canvas)
        self.__model = State(self)
        self.__modelDict = {}
        self.__commandName = ""

        
    def ChangeState(self, stateName: str):
        pass

    def execute(self):
        c = self.__canvas.getkey()
        
    def __draw():
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



        
    



      

    
