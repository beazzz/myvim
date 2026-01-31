from .Data import Command

class rightCommand(Command):
    """
    move cursor right
    """
    def execute(self, *args : None):
        self._editor.moveCursorRight(1)      
class leftCommand(Command):
    """
    move cursor left
    """
    def execute(self, *args: None):
        self._editor.moveCursorLeft(1)
class upCommand(Command):
    """
    move cursor up
    """
    def execute(self, *args: None):
        self._editor.moveCursorUp(1)
class downCommand(Command):
    """
    move cursor down
    """
    def execute(self, *args: None):
        self._editor.moveCursorDown(1)
class ZeroCommand(Command):
    """
    move Cursor ToStart String
    """
    def execute(self, *args: None):
        self._editor.moveCursorToStringStart()
class DollarCommand(Command):
    """
    move cursor to end string
    """
    def execute(self, *args: None):
        self._editor.moveCursorToStringEnd()

class moveCursorToRightWordEnd(Command):
        def execute(self, *args: None):
            self._editor.moveCursorToRightWordEnd()
class moveCursorToLeftWordStart(Command):
    def execute(self, *args: None):
        self._editor.moveCursorToLeftWordStart()
class moveCursorToFileStart(Command):
    def execute(self, *args: None):
        self._editor.moveCursorToFileStart()
class moveCursorToFileEnd(Command):
    def execute(self, *args: None):
        self._editor.moveCursorToFileEnd()
class moveCursorToNstring(Command):
    def execute(self, *args: int):
        """
        :param args: only 1 is N - number of string
        :type args: int
        """
        return self._editor.moveCursorToNstring(args[0])
class moveScreenToUp(Command):
    def execute(self, *args):
        self._editor.moveScreenToUp()
class moveScreenToDown(Command):
    def execute(self, *args):
        self._editor.moveScreenToDown()

class deleteWordAfterCursor(Command):
    def execute(self, *args: None):
        self._editor.deleteWordAfterCursor()
class deleteWordUnderCursor(Command):
    def execute(self, *args: None):
        self._editor.deleteWordUnderCursor()
class cutCurrentString(Command):
    def execute(self, *args: None):
        self._editor.cutCurrentString()
class copyCurrentString(Command):
    def execute(self, *args: None):
        self._editor.copyCurrentString()
class copyWordUnderCursor(Command):
    def execute(self, *args):
        self._editor.copyWordUnderCursor()
class pasteAfterCursor(Command):
    def execute(self, *args):
        self._editor.pasteAfterCursor()
