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
        # self.addCommand("/", Command.ChangeToStateSearch(self._context))
        self.addCommand("Error command", Command.ErrorCommand(self._context))

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
        self.addCommand("NG", Command.moveCursorToNstring(self._model))
        self.addCommand("KEY_A3", Command.moveScreenToUp(self._model)) # idk
        self.addCommand("KEY_C3", Command.moveScreenToDown(self._model)) # idk
        self.addCommand("x", Command.deleteSymbolAfterCursor(self._model))
        self.addCommand("diw", Command.deleteWordUnderCursor(self._model)) # probel(need  fix MyString find)
        self.addCommand("dd", Command.cutCurrentString(self._model))
        self.addCommand("yy", Command.copyCurrentString(self._model))
        self.addCommand("yw", Command.copyWordUnderCursor(self._model))
        self.addCommand("p", Command.pasteAfterCursor(self._model))

        self.__clear()

    def __clear(self):
        self.__num = ""
        self.__CommandName = ""

    def handleInput(self, ch: str) -> bool:
        print("Normal State, handleInput", ch)
        # print("handleInput", ch, "from", self)
        if  ch.isdigit() and  not self.__CommandName:
            if not self.__num:
                self.__CommandName+= 'N' # for detect number before command
            self.__num += ch
        else:
            self.__CommandName+= ch

        command = self._commands.get(self.__CommandName, "")
        if not command:
            for key in self._commands.keys():
                if self.__CommandName in key:
                    return False
            self.__clear()
            return False
        
        if self.__num:
            status = command.execute(int(self.__num))
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
        # self.addCommand("r", Command.replaceSymbolUnderCursor(self._model))

        self.__clear()

    def __clear(self):
        self.__commandName = ""

    def handleInput(self, ch) -> bool:
        print("InsertState: handleInput", ch)
        if self.__commandName:
            if ch == "\x1b": # is ESC?
                command = self._commands.get(ch)
                self.__clear()
                return command.execute()
            
            command = self._commands.get(self.__commandName)
            return command.execute(ch)
        else:
            command = self._commands.get(ch)
            if command:
                self.__commandName = 'i'
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
        self.addCommand("/text", Command.searchFromCursor(self._model))
        #self.addCommand("n", Command.research(self._model))
        #self.addCommand("N", Command.researchInvers(self._model))

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
        self.addCommand("set num", Command.TurnOnOffNumStrings(self._model))
        self.addCommand("h", Command.help(self._context))
        
        self.__clear()

    def __clear(self):
        self.__commandName = ""
        self.__arg = ""
    def __esc(self):
        self.__clear()
        command = self._commands.get('\x1b')
        return command.execute()

    def handleInput(self, ch):
        if ch == '\n': # enter
            if self.__commandName.isdigit(): # Command "number"
                command = self._commands.get("number")
                command.execute(int(self.__commandName))
                return self.__esc()
            parts = self.__commandName.split()
            if len(parts) >= 2: # Commands w/o filename
                self.__commandName = parts[0] + ' '
                self.__arg = parts[1]
            command = self._commands.get(self.__commandName)
            if command: # Other commands
                command.execute(self.__arg)
            return self.__esc()
        elif ch == '\x1b': # Command "esc"
            return self.__esc()

        self.__commandName += ch

        return True
        

