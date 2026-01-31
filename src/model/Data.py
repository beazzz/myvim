from view.View import View
from MyString import MyString



class Data:
    """
    There are data for vim. 
    For Command is Receiver, For State is Context
    """
    def __init__(self, url = None):
        # contructor
        print("Create", self)
        self.__posCursor = {'x': 0,
                            'y': 0}
        self.__view = View()
        self.__open(url)
        self.__states: dict[State] = {}
        self.__state = State(self)

    def handleInput(self, commandName : str):
        print("Data handle command", commandName, self)
        self.__state.handleInput(commandName)
    
    def posCursor(self, coord, value):
        print("Data change pos", coord, value, self)
        self.__posCursor[coord]+= value

    def getPosCursor(self):
        return self.__posCursor
    
    def ChangeState(self, stateName : str):
        state = self.__states.get(stateName)
        if state is None:
            print("State is incorrect")
            return
        self.__state = state
        print("ChangeState", stateName, self)\
        
    def AddState(self, stateName: str, state : State):
        self.__states[stateName] = state


    def __open(self, url : str):
        if url is not None:
            try:
                with open(url, 'r', encoding="utf-8") as file:
                    self.__string = [MyString(line.rstrip('\n')) for line in file.readlines()]
                for string in self.__string:
                    print(string.c_str())
                
            except FileNotFoundError:
                print("FileNotFound, please check correct path file!")
        else:
            self.__string = [MyString()]
    
class Command:
    """
    Parent for OtherCommands
    """
    def __init__(self, editor: Data):
        print("Create command", self)
        self._editor = editor

    def execute(self):
        print("Execute command", self)
        pass

class State:
    """
    Parent for OtherState
    For Command is Invoker
    """
    def __init__(self, context : Data):
        print("Create State", self)
        self._commands: dict[Command] = {}
        self._context = context
    
    def handleInput(self, commandName : str):
        """
        Pass control to Command
        """
        print("State handle command", commandName, self)
        self._commands[commandName].execute()
        
    def addCommmand(self, commandName : str, command: Command):
        print("State add command", commandName, self)
        self._commands[commandName] = command
        
    def ChangeState(self, stateName : str):
        print("State change state", stateName, self)
        self._context.ChangeState(stateName)
                                                                                                                              
# view = View()
# test = Data(view)
# test.posCursor('x', 10)
# print(test.getPosCursor())
