from .Data import State
import model.Command as Command

class NormalState(State):
    """
    state for navigate and edit
    """
    def __init__(self, context):
        super().__init__(context)
        self.addCommmand("right", Command.rightCommand(self._context))
        self.addCommmand("left", Command.leftCommand(self._context))
        self.addCommmand("up", Command.upCommand(self._context))
        self.addCommmand("down", Command.downCommand(self._context))
        self.addCommmand("0", Command.ZeroCommand(self._context))
        self.addCommmand("$", Command.DollarCommand(self._context))

        self.addCommmand("w", Command.moveCursorToRightWordEnd(self._context))
        self.addCommmand("b", Command.moveCursorToLeftWordStart(self._context))
        self.addCommmand("gg", Command.moveCursorToFileStart(self._context))
        self.addCommmand("G", Command.moveCursorToFileEnd(self._context))
        self.addCommmand("NG", Command.moveCursorToNstring(self._context))
        self.addCommmand("PG_UP", Command.moveScreenToUp(self._context))
        self.addCommmand("PG_DOWN", Command.moveScreenToDown(self._context))
        self.addCommmand("x", Command.deleteWordAfterCursor(self._context))
        self.addCommmand("diw", Command.deleteWordUnderCursor(self._context))
        self.addCommmand("dd", Command.cutCurrentString(self._context))
        self.addCommmand("yy", Command.copyCurrentString(self._context))
        self.addCommmand("yw", Command.copyWordUnderCursor(self._context))
        self.addCommmand("p", Command.pasteAfterCursor(self._context))
        

class InsertState(State):
    pass

class VisualState(State):
    pass

class CommandState(State):
    pass

