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
        self.__state = State(self)

    def handleInput(self, commandName):
        print("Data handle command", commandName, self)
        self.__state.handleInput(commandName)
    
    def posCursor(self, coord, value):
        print("Data change pos", coord, value, self)
        self.__posCursor[coord]+= value

    def getPosCursor(self):
        return self.__posCursor
    
    def SetState(self, state : State):
        print("SetState", state, self)
        self.__state = state


    def __open(self, url):
        if url is not None:
            try:
                with open(url, 'r', encoding="utf-8") as file:
                    self.__string = MyString(file.read())
                print(self.__string.c_str())
            except FileNotFoundError:
                print("FileNotFound, please check correct path file!")
        else:
            self.__string = MyString()
    
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
    
    def handleInput(self, commandName):
        """
        Pass control to Command
        """
        print("State handle command", commandName, self)
        self._commands[commandName].execute()
        
    def addCommmand(self, commandName, command: Command):
        print("State add command", commandName, self)
        self._commands[commandName] = command
        
    def ChangeState(self, state: State):
        print("State change state", state, self)
        self._context.SetContext(state)
                                                                                                                              
# view = View()
# test = Data(view)
# test.posCursor('x', 10)
# print(test.getPosCursor())
