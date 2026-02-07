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
        self.open(url)
        # self.__states: dict[State] = {}
        # self.__state = State(self)
        self.__buffer = MyString()
        self.__url : str = None
        self.__editStatus = False
    def __str__(self):
        return "\n".join(string.c_str() for string in self.__string)
    
    # def handleInput(self, commandName : str, *args):
    #     print("Data handle command", commandName)
    #     return self.__state.handleInput(commandName, *args)
    # def AddState(self, stateName: str, state : 'State'):
    #     self.__states[stateName] = state
    # def ChangeState(self, stateName : str):
    #     state = self.__states.get(stateName)
    #     if state is None:
    #         print("State is incorrect")
    #         return
    #     self.__state = state
    #     print("ChangeState", stateName, self)

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
        print("right completed")
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
        print("left completed")

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
        self.__posCursor['x'] = self.__posCursor['y'] = self.__posCursor['x_save'] = 0
    def moveCursorToFileEnd(self):
        self.__posCursor['y'] = self.getCountOfColumn()-1
        self.__posCursor['x_save'] = self.__posCursor['x'] = self.getLenString()
    def moveCursorToNstring(self, N : int):
        if (N < 0 or N > self.getCountOfColumn()):
            raise ValueError("N is not valid")
        self.__posCursor['x_save'] = self.__posCursor['x'] = 0
        self.__posCursor['y'] = N-1
    def moveScreenToUp(self):
        pass
    def moveScreenToDown(self):
        pass
    def deleteSymbolAfterCursor(self):
        self.__string[self.__posCursor['y']].erase(self.__posCursor['x'], 1)

        self.__SetEditFile()
    def deleteWordUnderCursor(self):
        """
        incorrect find in MyString
        """
        len = self.__string[self.__posCursor['y']].find(" ", self.__posCursor['x'])
        # if len == -1:
        #     len = self.getLenString()
        len = len - self.__posCursor['x']
        self.__string[self.__posCursor['y']].erase(self.__posCursor['x'], len)

        self.__SetEditFile()
    def cutCurrentString(self, NumString = None):
        if NumString is None:
            NumString = self.__posCursor['y']
        self.buffer = self.__string.pop(NumString)

        self.__SetEditFile()
    def copyCurrentString(self, NumString = None):
        if NumString is None:
            NumString = self.__posCursor['y']
        self.__buffer = self.__string[NumString]
    def copyWordUnderCursor(self):
        len = self.__string[self.__posCursor['y']].find(" ", self.__posCursor['x'])
        # if len == -1:
        #     len = self.getLenString()
        len = len - self.__posCursor['x']
        self.__buffer = self.__string[self.__posCursor['y']].substr(self.__posCursor['x'], len)
    def pasteAfterCursor(self):
        NumString = self.__posCursor['y']
        index = self.__posCursor['x']
        self.__string[NumString].insert(index, self.__buffer)

        self.__SetEditFile()
    def deleteCurrentString(self):
        self.__string[self.__posCursor['y']].clear()
        self.moveCursorToStringStart()

        self.__SetEditFile()

    # For insert mode
    def insertText(self, text : str):
        """
        Insert text after cursor
        """
        self.__string[self.__posCursor['y']].insert(self.__posCursor['x'], text)

        self.__SetEditFile()
    def insertTextInStartString(self, text: str):
        """
        Go to start string and insert text
        """
        self.moveCursorToStringStart()
        self.insertText(text)
    def insertTextInEndString(self, text: str):
        """
        Docstring for insertTextInEndString
        
        Go to string end and insert
        """
        self.moveCursorToStringEnd()
        self.insertText(text) 
    def deleteStringToInsert(self, text: str):
        """
        detete String and insert
        """
        self.deleteCurrentString()
        self.insertText(text)
    def replaceSymbolUnderCursor(self, symbol: str):
        """
        Docstring for replaceSymbolUnderCursor
        :describe: replace symbol on current cursor
        :param text: 1 symbol
        :type text: str
        """
        if (len(symbol) != 1):
            raise ValueError("Symbol is incorrect")
        self.deleteSymbolAfterCursor()
        self.insertText(symbol)

    # fixk pybind
    def searchFromCursor(self, text: str):
        """
        Docstring for searchFromCursoro
     
        :param text: Text is searched
        :type text: str
        :return: None
        :rtype: -
        """
        # cursor = self.getPosCursor()
        # string = self.__string[self.__posCursor['y']].substr(self.__posCursor['x'])
        # index = string.find(text)
        # if (index == True):
        #     self.moveCursorRight(index + self.__posCursor['x'])
        #     return
        
        # while index == False and self.__isEndFile() == False:
        #     self.moveCursorToStringEnd()
        #     self.moveCursorRight(1)
        #     index = self.__string[self.__posCursor['y']].find(text)

        # if (index == False):
        #     self.SetPosCursor(cursor)
        pass
    
    # For Command state
    def open(self, url : str):
        if url is not None:
            try:
                with open(url, 'r', encoding="utf-8") as file:
                    self.__string = [MyString(line.rstrip('\n')) for line in file.readlines()]
                    self.__url = url
                # for string in self.__string:
                #     print(string.c_str())
                #self.printAllStrings()
                
            except FileNotFoundError:
                print("FileNotFound, please check correct path file!")
        else:
            self.__string = [MyString()]
    def writeFile(self, url : str = None):
        if url is None:
            url = self.__url
        
        strings = ""
        for string in self.__string:
            strings += string.c_str() + '\n'
        strings = strings[:-1]
           
        with open(url, "w", encoding="utf-8") as file:
            file.write(strings)
    def quit(self, must = None):
        if must is not None:
            pass
        else:
            if (self.__editStatus() == False):
                print("Exit File")
            else:
                print("Cant exit. Use q!")
    def writeQuit(self):
        self.writeFile()
        self.quit(True)
    def showHelp(self):
        for command in self.__state._commands:
            print(command)
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
    def __doCorrectCursor(self):
        """
        observing Cursor's coord after up and down command
        """
        end_string = self.getLenString()#len(self.getRaw())
        if self.__posCursor['x_save'] > end_string:
            self.__posCursor['x'] = end_string
        else:
            self.__posCursor['x'] = self.__posCursor['x_save']
    def __SetEditFile(self):
        self.__editStatus = True

class Command:
    """
    Parent for OtherCommands
    """
    def __init__(self, editor: Data):
        #print("Create command", self)
        self._editor = editor

    def execute(self, *args) -> bool:
        #print("Execute command", self)
        return False
class State:
    """
    Parent for OtherState
    For Command is Invoker
    """
    def __init__(self, context : Data):
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
                                                                                                                              
