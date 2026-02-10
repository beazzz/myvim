from .Core import State
import controller.Command as Command

class ObserverState(State):
    """
    Help to change state
    """

    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand(":", Command.ChangeToStateCommand(self._context))
        self.addCommand("\x1b", Command.ChangeToStateNormal(self._context))

        self.addCommand("/", Command.ChangeToStateSearch(self._context))
        self.addCommand("?", Command.ChangeToStateSearch(self._context))
        self.addCommand("n", Command.ChangeToStateSearch(self._context))
        self.addCommand("N", Command.ChangeToStateSearch(self._context))
        # self.addCommand("Error command", Command.ErrorCommand(self._context))

        self.addCommand("i", Command.ChangeToStateInsert(self._context))
        self.addCommand("I", Command.ChangeToStateInsert(self._context))
        self.addCommand("A", Command.ChangeToStateInsert(self._context))
        self.addCommand("S", Command.ChangeToStateInsert(self._context))
        # self.addCommand("r", Command.ChangeToStateInsert(self._context))


class NormalState(ObserverState):
    """
    state for navigate and edit
    """
    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand("KEY_B3", Command.moveCursorRight(self._model))
        self.addCommand("KEY_B1", Command.moveCursorLeft(self._model))
        self.addCommand("KEY_A2", Command.moveCursorUp(self._model))
        self.addCommand("KEY_C2", Command.moveCursorDown(self._model))
        self.addCommand("^", Command.moveCursorToStartString(self._model))
        self.addCommand("$", Command.moveCursorToEndString(self._model))
        self.addCommand("w", Command.moveCursorToRightWordEnd(self._model))
        self.addCommand("b", Command.moveCursorToLeftWordStart(self._model))
        self.addCommand("gg", Command.moveCursorToFileStart(self._model))
        self.addCommand("G", Command.moveCursorToFileEnd(self._model))
        self.addCommand(" G", Command.moveCursorToNstring(self._model))
        self.addCommand("x", Command.deleteSymbolAfterCursor(self._model))
        self.addCommand("diw", Command.deleteWordUnderCursor(self._model))
        self.addCommand("dd", Command.cutCurrentString(self._model))
        self.addCommand("yy", Command.copyCurrentString(self._model))
        self.addCommand("yw", Command.copyWordUnderCursor(self._model))
        self.addCommand("p", Command.pasteAfterCursor(self._model))

        self.__clear()

    def __clear(self):
        self._arg = ""
        self._commandName = ""

    def handleInput(self, ch: str) -> bool:
        if  ch.isdigit() and  not self._commandName:
            if not self._arg:
                self._commandName+= ' ' # for detect number before command
            self._arg += ch
        elif ch.isdigit() and self._commandName == ' ':
            self._arg += ch
        else:
            self._commandName+= ch

        command = self._commands.get(self._commandName)
        if not command:
            for key in self._commands.keys():
                if self._commandName in key:
                    return False
            self.__clear()
            return False
        
        if self._arg:
            status = command.execute(int(self._arg))
        else:
            status = command.execute(ch)
        self.__clear()
        return status

class InsertState(ObserverState):
    """
    State for insert text
    """
    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand("i", Command.insertText(self._model))
        self.addCommand("I", Command.insertTextInStartString(self._model))
        self.addCommand("A", Command.insertTextInEndString(self._model))
        self.addCommand("S", Command.deleteStringToInsert(self._model))
        self.addCommand("\x08", Command.deleteSymbolAfterCursor(self._model))
        # self.addCommand("r", Command.replaceSymbolUnderCursor(self._model))

        self.__clear()

    def __clear(self):
        self._commandName = ""

    def handleInput(self, ch) -> bool:
        # print("InsertState: handleInput", ch)
        if self._commandName:
            if ch == "\x1b": # is ESC?
                command = self._commands.get(ch)
                self.__clear()
                return command.execute()
            if ch == "\x08": # BackSpace
                command = self._commands.get(ch)
                return command.execute()
            
            command = self._commands.get(self._commandName)
            return command.execute(ch)
        else:
            command = self._commands.get(ch)
            if command:
                self._commandName = 'i'
                if ch != 'i':
                    return command.execute()
                return True
            return False

class SearchState(ObserverState):
    """
    State for search text
    """
    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand("/", Command.searchFromCursorToEndFile(self._model))
        self.addCommand("?", Command.searchFromCursorToStartFile(self._model))
        self.addCommand("n", Command.research(self._model))
        self.addCommand("N", Command.researchInvers(self._model))

        self.__clear()

    def __clear(self):
        self._commandName = ""

    def __esc(self):
        self.__clear()
        command = self._commands.get('\x1b')
        return command.execute()

    def handleInput(self, ch):
        if ch == '\n': # enter
            print(self._commandName)
            if (self._commandName[0] == '/' or self._commandName[0] == '?'):
                self._arg = self._commandName[1:]
            self._commandName =  self._commandName[0]
            command = self._commands.get(self._commandName)
            if command: # Other commands
                command.execute(self._arg)

            return self.__esc()
        elif ch == '\x1b': # Command "esc"
            return self.__esc()

        self._commandName += ch

        return True

class CommandState(ObserverState):
    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand("o ", Command.open(self._model))
        self.addCommand("x", Command.writeExit(self._model))
        self.addCommand("w", Command.write(self._model))
        self.addCommand("w ", Command.writeFile(self._model))
        self.addCommand("q", Command.quitAfterSave(self._model))
        self.addCommand("q!", Command.quitWithoutSave(self._model))
        self.addCommand("wq!", Command.writeQuit(self._model))
        self.addCommand("number", Command.placeNstring(self._model))
        self.addCommand("set", Command.TurnOnOffNumStrings(self._model))
        self.addCommand("h", Command.help(self._context))
        
        # self.__clear()
        # self._commandName = ":"

    def __clear(self):
        self._commandName = ""
        self._arg = ""
    def __esc(self):
        self.__clear()
        command = self._commands.get('\x1b')
        return command.execute()

    def handleInput(self, ch):
        if ch == '\n': # enter
            self._commandName = self._commandName[1:]
            if self._commandName.isdigit(): # Command "number"
                command = self._commands.get("number")
                command.execute(int(self._commandName))
                return self.__esc()
            parts = self._commandName.split()
            if len(parts) >= 2: # Commands w/o filename
                self._commandName = parts[0] + ' '
                self._arg = parts[1]
            command = self._commands.get(self._commandName)
            print(self._commandName, self._arg)
            if command: # Other commands
                command.execute(self._arg)
            return self.__esc()
        elif ch == '\x1b': # Command "esc"
            return self.__esc()

        self._commandName += ch

        return True
        

