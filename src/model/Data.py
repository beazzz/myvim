from view.View import View
from MyString import MyString



class Data:
    """
    There are data for vim. 
    For Command is Receiver, For State is Context
    """
    def __init__(self, url = None):
        # contructor
        #print("Create", self)
        self.__posCursor = {'x': 0,
                            'y': 0,
                            'x_save': 0}
        self.__view = View()
        self.__open(url)
        self.__states: dict[State] = {}
        self.__state = State(self)

    def handleInput(self, commandName : str):
        print("Data handle command", commandName, self)
        self.__state.handleInput(commandName)
    def AddState(self, stateName: str, state : State):
        self.__states[stateName] = state
    def ChangeState(self, stateName : str):
        state = self.__states.get(stateName)
        if state is None:
            print("State is incorrect")
            return
        self.__state = state
        #print("ChangeState", stateName, self)

    def SetPosCursor(self, dictOfCoord : dict):
        self.__posCursor = dictOfCoord

    def getPosCursor(self):
        return self.__posCursor
    def getSymbol(self):
        return self.__string[self.__posCursor['y']][self.__posCursor['x']]
    def getRaw(self):
        string = self.__string[self.__posCursor['y']]
        return string.c_str()
    def getCountOfColumn(self):
        return len(self.__string)
    def getLenString(self):
        return self.__string[self.__posCursor['y']].size()
    def moveCursorRight(self, value : int):
        endString = self.getLenString()
        self.__posCursor['x'] += value

        if (self.__isEndFile()):
            self.__posCursor['x'] = endString
        elif (self.__posCursor['x'] > endString):
            self.moveCursorDown(1)
            self.__posCursor['x'] = 0

        self.__posCursor['x_save'] = self.__posCursor['x']
        print("right completed",self)
    def moveCursorLeft(self, value : int):
        self.__posCursor['x'] -= value

        if self.__posCursor['x'] < 0:
            # is first column?
            if self.__posCursor['y'] == 0:
                self.__posCursor['x'] = 0
            else:
                self.moveCursorUp(1)
                self.__posCursor['x'] = self.getLenString()

        self.__posCursor['x_save'] = self.__posCursor['x']
        print("left completed", self)

    def moveCursorUp(self, value: int):
        self.__posCursor['y'] -= value
        if self.__posCursor['y'] < 0:
            self.__posCursor['y'] = 0
        
        self.__doCorrectCursor()
    def moveCursorDown(self, value: int):
        self.__posCursor['y'] += value
        value = self.getCountOfColumn() - 1
        if self.__posCursor['y'] > value:
            self.__posCursor['y'] = value

        self.__doCorrectCursor()
    def moveCursorToStringStart(self):
        self.__posCursor['x'] = 0
    def moveCursorToStringEnd(self):
        self.__posCursor['x'] = self.getLenString()
    def moveCursorToRightWordEnd(self):
        # move from cur pos
        self.moveCursorRight(1)
        # skip space
        while (self.__string[self.__posCursor['y']][self.__posCursor['x']] == ' '):
            self.moveCursorRight(1)
        # go to end
        while (
            self.__string[self.__posCursor['y']][self.__posCursor['x']] != ' ' and
            self.__IsEndString() == False
            ):
            self.moveCursorRight(1)

    def moveCursorToLeftWordStart(self):
        self.moveCursorLeft(1)
        # skip space 
        while (
            (self.__string[self.__posCursor['y']][self.__posCursor['x']] == ' ' or
            self.__string[self.__posCursor['y']][self.__posCursor['x']] == '\0') and
            self.__isStartString() == False
               ):
            self.moveCursorLeft(1)

        # go to start 
        while (
            self.__string[self.__posCursor['y']][self.__posCursor['x']] != ' ' and
            self.__string[self.__posCursor['y']][self.__posCursor['x']] != '\0' and
            self.__isStartString() == False
            ):
            self.moveCursorLeft(1)

        while (
            self.__string[self.__posCursor['y']][self.__posCursor['x']] == ' ' or
            self.__string[self.__posCursor['y']][self.__posCursor['x']] == '\0'
               ):
            self.moveCursorRight(1)
        

    def moveCursorToFileStart(self):
        pass
    def moveCursorToFileEnd(self):
        pass
    def moveCursorToNstring(self, N : int):
        pass
    def moveScreenToUp(self):
        pass
    def moveScreenToDown(self):
        pass
    def deleteWordAfterCursor(self):
        pass
    def deleteWordUnderCursor(self):
        pass
    def cutCurrentString(self):
        pass
    def copyCurrentString(self):
        pass
    def copyWordUnderCursor(self):
        pass
    def pasteAfterCursor(self):
        pass


    def __isStartString(self):
        """
        return true if it is start
        """
        return self.__posCursor['x'] == 0
    def __IsEndString(self):
        """
        return true if it is end
        """
        return self.getSymbol() == '\0'
    def __isEndFile(self):
        """
        return true if it is enf file
        """
        cursor = self.getPosCursor()
        return cursor['x'] >= self.getLenString() and cursor['y'] == self.getCountOfColumn()-1

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
    def __doCorrectCursor(self):
        """
        observing Cursor's coord after up and down command
        """
        end_string = self.getLenString()#len(self.getRaw())
        if self.__posCursor['x_save'] > end_string:
            self.__posCursor['x'] = end_string
        else:
            self.__posCursor['x'] = self.__posCursor['x_save']

class Command:
    """
    Parent for OtherCommands
    """
    def __init__(self, editor: Data):
        #print("Create command", self)
        self._editor = editor

    def execute(self, *args):
        #print("Execute command", self)
        pass

class State:
    """
    Parent for OtherState
    For Command is Invoker
    """
    def __init__(self, context : Data):
        #print("Create State", self)
        self._commands: dict[Command] = {}
        self._context = context
    
    def handleInput(self, commandName : str):
        """
        Pass control to Command
        """
        #print("State handle command", commandName, self)
        self._commands[commandName].execute()
        
    def addCommmand(self, commandName : str, command: Command):
        #print("State add command", commandName, self)
        self._commands[commandName] = command
        
    def ChangeState(self, stateName : str):
        #print("State change state", stateName, self)
        self._context.ChangeState(stateName)
                                                                                                                              
