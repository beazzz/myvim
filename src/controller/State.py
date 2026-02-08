from .Core import State
import controller.Command as Command

class ObserverState(State):
    """
    Help to change state
    """

    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand(":", Command.ChangeToStateCommand(self._model))
        self.addCommand("esc", Command.ChangeToStateNormal(self._model))
        self.addCommand("/", Command.ChangeToStateSearch(self._model))
        self.addCommand("Error command", Command.ErrorCommand(self._model))

        self.addCommand("i", Command.ChangeToStateInsert(self._model))
        self.addCommand("I", Command.ChangeToStateInsert(self._model))
        self.addCommand("A", Command.ChangeToStateInsert(self._model))
        self.addCommand("S", Command.ChangeToStateInsert(self._model))
        self.addCommand("r", Command.ChangeToStateInsert(self._model))

class NormalState(ObserverState):
    """
    state for navigate and edit
    """
    def __init__(self, context, model):
        super().__init__(context, model)
        self.addCommand("right", Command.moveCursorRight(self._model))
        self.addCommand("left", Command.moveCursorLeft(self._model))
        self.addCommand("up", Command.moveCursorUp(self._model))
        self.addCommand("down", Command.moveCursorDown(self._model))
        self.addCommand("0", Command.moveCursorToStartString(self._model))
        self.addCommand("$", Command.moveCursorToEndString(self._model))
        self.addCommand("w", Command.moveCursorToRightWordEnd(self._model))
        self.addCommand("b", Command.moveCursorToLeftWordStart(self._model))
        self.addCommand("gg", Command.moveCursorToFileStart(self._model))
        self.addCommand("G", Command.moveCursorToFileEnd(self._model))
        self.addCommand("NG", Command.moveCursorToNstring(self._model))
        self.addCommand("PG_UP", Command.moveScreenToUp(self._model))
        self.addCommand("PG_DOWN", Command.moveScreenToDown(self._model))
        self.addCommand("x", Command.deleteSymbolAfterCursor(self._model))
        self.addCommand("diw", Command.deleteWordUnderCursor(self._model))
        self.addCommand("dd", Command.cutCurrentString(self._model))
        self.addCommand("yy", Command.copyCurrentString(self._model))
        self.addCommand("yw", Command.copyWordUnderCursor(self._model))
        self.addCommand("p", Command.pasteAfterCursor(self._model))

        self.num = ""
        self.CommandName = ""
    def handleInput(self, ch: str) -> bool:
        print("handleInput", ch, "from", self)
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
        try:
            return command.execute([int(self.num)])
        except ValueError:
            return command.execute([0])

        
class InsertState(ObserverState):
    """
    State for insert text
    """
    def __init__(self, context, model):
        super().__init__(context, model)
        # self.addCommand("i", Command.insertText(self._model))
        # self.addCommand("I", Command.insertTextInStartString(self._model))
        # self.addCommand("A", Command.insertTextInEndString(self._model))
        # self.addCommand("S", Command.deleteStringToInsert(self._model))
        # self.addCommand("r", Command.replaceSymbolUnderCursor(self._model))

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

