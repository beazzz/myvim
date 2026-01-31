from view.View import View
from MyString import MyString



class Data:
    def __init__(self):
        # contructor
        print("Create", self)
        self.__posCursor = {'x': 0,
                            'y': 0}
        self.__view = View()
        self.__string = MyString()
        self.__state = State(self)

    def handleInput(self, commandName):
        print("Data handle command", commandName, self)
        self.__state.handleInput(commandName)
    
    def posCursor(self, coord, value):
        print("Data change pos", coord, value, self)
        self.__posCursor[coord]+= value

    def getPosCursor(self):
        return self.__posCursor
    
    def SetContext(self, state : State):
        print("SetContext", state, self)
        self.__state = state
    
class Command:
    def __init__(self, editor: Data):
        print("Create command", self)
        self._editor = editor

    def execute(self):
        print("Execute command", self)
        pass

class State:
    def __init__(self, context : Data):
        print("Create State", self)
        self._commands: dict[Command] = {}
        self._context = context
    
    def handleInput(self, commandName):
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
