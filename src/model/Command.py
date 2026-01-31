from .Data import Command

class rightCommand(Command):
    """
    move cursor right
    """
    def execute(self):
        self._editor.moveCursorRight(1)
        
class leftCommand(Command):
    """
    move cursor left
    """
    def execute(self):
        self._editor.moveCursorLeft(1)
class upCommand(Command):
    """
    move cursor up
    """
    def execute(self):
        self._editor.moveCursorUp(1)
class downCommand(Command):
    """
    move cursor down
    """
    def execute(self):
        self._editor.moveCursorDown(1)
class ZeroCommand(Command):
    """
    move Cursor ToStart String
    """
    def execute(self):
        self._editor.moveCursorToStringStart()
class DollarCommand(Command):
    """
    move cursor to end string
    """
    def execute(self):
        self._editor.moveCursorToStringEnd()

class moveCursorToRightWordEnd(Command):
        def execute(self):
            self._editor.moveCursorToRightWordEnd()
class moveCursorToLeftWordStart(Command):
    pass
class moveCursorToFileStart(Command):
    pass
class moveCursorToFileEnd(Command):
    pass
class moveCursorToNstringUP(Command):
    pass
class moveCursorToNstringDown(Command):
    pass
class deleteWordAfterCursor(Command):
    pass
class deleteWordUnclassCursor(Command):
    pass
class cutCurrentString(Command):
    pass
class copyCurrentString(Command):
    pass
class copyWordUnderCursor(Command):
    pass
class pasteAfterCursor(Command):
    pass
