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
        self.addCommand("Error command", Command.ErrorCommand(self._context))

        self.addCommand("i", Command.ChangeToStateInsert(self._context))
        self.addCommand("I", Command.ChangeToStateInsert(self._context))
        self.addCommand("A", Command.ChangeToStateInsert(self._context))
        self.addCommand("S", Command.ChangeToStateInsert(self._context))
        self.addCommand("r", Command.ChangeToStateInsert(self._context))

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

        self.__num = ""
        self.__CommandName = ""
    def handleInput(self, ch: str) -> bool:
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
            self.__CommandName = ""
            self.__num = ""
            return False
        
        if self.__num:
            status = command.execute(int(self.__num))
        else:
            status = command.execute()
        self.__CommandName = ""
        self.__num = ""
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
        self.addCommand("r", Command.replaceSymbolUnderCursor(self._model))
    def handleInput(self, ch) -> bool:
        if (ch == "esc"):
            command = self._commands.get(ch)
        else:
            command = self._commands.get('i')
        return command.execute(ch)

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
        self.addCommand("o", Command.open(self._model))
        self.addCommand("x", Command.writeExit(self._model))
        self.addCommand("w", Command.write(self._model))
        self.addCommand("w filename", Command.writeFile(self._model))
        self.addCommand("q", Command.quitAfterSave(self._model))
        self.addCommand("q!", Command.quitWithoutSave(self._model))
        self.addCommand("wq!", Command.writeQuit(self._model))
        self.addCommand("number", Command.placeNstring(self._model))
        self.addCommand("set num", Command.TurnOnOffNumStrings(self._model))
        self.addCommand("h", Command.help(self._model))

