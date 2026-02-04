from .Data import Command
"""
Normal Mode
"""
class moveCursorRight(Command):
    """
    move cursor right
    """
    def execute(self, *args : None):
        self._editor.moveCursorRight(1)      
class moveCursorLeft(Command):
    """
    move cursor left
    """
    def execute(self, *args: None):
        self._editor.moveCursorLeft(1)
class moveCursorUp(Command):
    """
    move cursor up
    """
    def execute(self, *args: None):
        self._editor.moveCursorUp(1)
class moveCursorDown(Command):
    """
    move cursor down
    """
    def execute(self, *args: None):
        self._editor.moveCursorDown(1)
class moveCursorToStartString(Command):
    """
    move Cursor ToStart String
    """
    def execute(self, *args: None):
        self._editor.moveCursorToStringStart()
class moveCursorToEndString(Command):
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
class deleteSymbolAfterCursor(Command):
    def execute(self, *args: None):
        self._editor.deleteSymbolAfterCursor()
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

"""
Insert Mode
"""
class insertText(Command):
    def  execute(self, *args):
        self._editor.insertText(args[0])
class insertTextInStartString(Command):
    def  execute(self, *args):
        self._editor.insertTextInStartString(args[0])
class insertTextInEndString(Command):
    def  execute(self, *args):
        self._editor.insertTextInEndString(args[0])
class deleteStringToInsert(Command):
    def  execute(self, *args):
        self._editor.deleteStringToInsert(args[0])
class replaceSymbolUnderCursor(Command):
    def  execute(self, *args):
        self._editor.replaceSymbolUnderCursor(args[0])

"""
Search State
"""
class searchFromCursor(Command):
    """
    if find text Cursor will place in start text
    """
    def execute(self, *args):
        self._editor.searchFromCursor(args[0])
        
class research(Command):
    """
    repeat search
    """
    def execute(self, *args):
        pass
class researchInvers(Command):
    """
    search on the contrary 
    """
    def execute(self, *args):
        pass

"""
Command State
"""
class open(Command):
    def execute(self, *args):
        pass
class writeExit(Command):
    def execute(self, *args):
        pass
class write(Command):
    def execute(self, *args):
        pass
class writeFile(Command):
    def execute(self, *args):
        pass
class quitAfterSave(Command):
    def execute(self, *args):
        pass
class quitWithoutSave(Command):
    def execute(self, *args):
        pass
class writeQuit(Command):
    def execute(self, *args):
        pass
class placeNstring(Command):
    def execute(self, *args):
        pass
class TurnOnOffNumStrings(Command):
    def execute(self, *args):
        pass
class help(Command):
    def execute(self, *args):
        pass


