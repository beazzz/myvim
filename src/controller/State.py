from .Core import State
import controller.Command as Command

class ObserverState(State):
    """
    Help to change state
    """

    def __init__(self, context):
        super().__init__(context)
        self.addCommmand(":", Command.ChangeToStateCommand(self._context))
        self.addCommmand("esc", Command.ChangeToStateNormal(self._context))
        self.addCommmand("/", Command.ChangeToStateSearch(self._context))
        self.addCommand("Error command", Command.ErrorCommand(self._context))

        self.addCommmand("i", Command.ChangeToStateInsert(self._context))
        self.addCommmand("I", Command.ChangeToStateInsert(self._context))
        self.addCommmand("A", Command.ChangeToStateInsert(self._context))
        self.addCommmand("S", Command.ChangeToStateInsert(self._context))
        self.addCommmand("r", Command.ChangeToStateInsert(self._context))

class NormalState(ObserverState):
    """
    state for navigate and edit
    """
    def __init__(self, context):
        super().__init__(context)
        self.addCommmand("right", Command.moveCursorRight(self._context))
        self.addCommmand("left", Command.moveCursorLeft(self._context))
        self.addCommmand("up", Command.moveCursorUp(self._context))
        self.addCommmand("down", Command.moveCursorDown(self._context))
        self.addCommmand("0", Command.moveCursorToStartString(self._context))
        self.addCommmand("$", Command.moveCursorToEndString(self._context))
        self.addCommmand("w", Command.moveCursorToRightWordEnd(self._context))
        self.addCommmand("b", Command.moveCursorToLeftWordStart(self._context))
        self.addCommmand("gg", Command.moveCursorToFileStart(self._context))
        self.addCommmand("G", Command.moveCursorToFileEnd(self._context))
        self.addCommmand("NG", Command.moveCursorToNstring(self._context))
        self.addCommmand("PG_UP", Command.moveScreenToUp(self._context))
        self.addCommmand("PG_DOWN", Command.moveScreenToDown(self._context))
        self.addCommmand("x", Command.deleteSymbolAfterCursor(self._context))
        self.addCommmand("diw", Command.deleteWordUnderCursor(self._context))
        self.addCommmand("dd", Command.cutCurrentString(self._context))
        self.addCommmand("yy", Command.copyCurrentString(self._context))
        self.addCommmand("yw", Command.copyWordUnderCursor(self._context))
        self.addCommmand("p", Command.pasteAfterCursor(self._context))

        self.num = ""
        self.CommandName = ""
    def handleInput(self, ch: str) -> bool:
        if ch.isdigit() and  not self.CommandName:
            self.num += ch
        else:
            self.CommandName+= ch

        command = self._commands.get(self.CommandName, "")
        if not command:
            for key in self._commands.keys():
                if self.CommandName in key:
                    return False
            self.CommandName = ""
            self.num = ""
            return False

        return command.execute(int(self.num))

        
class InsertState(ObserverState):
    """
    State for insert text
    """
    def __init__(self, context):
        super().__init__(context)
        # self.addCommmand("i", Command.insertText(self._context))
        # self.addCommmand("I", Command.insertTextInStartString(self._context))
        # self.addCommmand("A", Command.insertTextInEndString(self._context))
        # self.addCommmand("S", Command.deleteStringToInsert(self._context))
        # self.addCommmand("r", Command.replaceSymbolUnderCursor(self._context))

class SearchState(ObserverState):
    """
    State for search text
    """
    def __init__(self, context):
        super().__init__(context)
        self.addCommmand("/text", Command.searchFromCursor(self._context))
        #self.addCommmand("n", Command.research(self._context))
        #self.addCommmand("N", Command.researchInvers(self._context))

class CommandState(ObserverState):
    def __init__(self, context):
        super().__init__(context)
        self.addCommmand("o", Command.open(self._context))
        self.addCommmand("x", Command.writeExit(self._context))
        self.addCommmand("w", Command.write(self._context))
        self.addCommmand("w filename", Command.writeFile(self._context))
        self.addCommmand("q", Command.quitAfterSave(self._context))
        self.addCommmand("q!", Command.quitWithoutSave(self._context))
        self.addCommmand("wq!", Command.writeQuit(self._context))
        self.addCommmand("number", Command.placeNstring(self._context))
        self.addCommmand("set num", Command.TurnOnOffNumStrings(self._context))
        self.addCommmand("h", Command.help(self._context))

