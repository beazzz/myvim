from view.View import View
from MyString import MyString



class Data:
    def __init__(self, view: View, state: State):
        # contructor
        self.__posCursor = {'x': 0,
                            'y': 0}
        self.__view = view 
        self.__string = MyString()
        self.__state = state

    def handleInput(self, commandName):
        print("Data handle command")
        self.__state.handleInput(commandName)
    
    def posCursor(self, coord, value):
        print("Data change pos")
        self.__posCursor[coord]+= value

    def getPosCursor(self):
        return self.__posCursor
    
    def SetContext(self, state : State):
        self.__state = state
    
class Command:
    def __init__(self, editor: Data):
        self._editor = editor

    def execute(self):
        pass

class State:
    def __init__(self, context : Data):
        self._commands: dict[Command] = {}
        self._context = context
    
    def handleInput(self, commandName):
        print("State handle command")
        self._commands[commandName].execute()
        
    def addCommmand(self, commandName, command: Command):
        print("State add command")
        self._commands[commandName] = command
        
    def ChangeState(self, state: State):
        print("State change state")
        self._context.SetContext(state)
                                                                                                                              
# view = View()
# test = Data(view)
# test.posCursor('x', 10)
# print(test.getPosCursor())
