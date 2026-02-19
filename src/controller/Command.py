from .Core import Command
"""
Observer
"""
class ChangeToStateNormal(Command):
    def execute(self, *args) -> bool:
        print("ChangeToStateNormal")
        return self._editor.ChangeState("Normal")
class ChangeToStateInsert(Command):
    def execute(self, *args)-> bool:
        print("ChangeToStateInsert")
        return self._editor.ChangeState("Insert", args[0])
class ChangeToStateSearch(Command):
    def execute(self, *args)-> bool:
        print("ChangeToStateSearch")
        return self._editor.ChangeState("Search", args[0])
class ChangeToStateCommand(Command):
    def execute(self, *args)-> bool:
        print("ChangeToStateCommand")
        return self._editor.ChangeState("Command", args[0])
class ErrorCommand(Command):
    def execute(self, *args)-> bool:
        return False

"""
Normal Mode
"""
class moveCursorRight(Command):
    """
    move cursor right
    """
    def execute(self, *args : None)-> bool:
        print("moveCursorRight")
        return self._editor.moveCursorRight(1)      
class moveCursorLeft(Command):
    """
    move cursor left
    """
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorLeft(1)
class moveCursorUp(Command):
    """
    move cursor up
    """
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorUp(1)
class moveCursorDown(Command):
    """
    move cursor down
    """
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorDown(1)
class moveCursorToStartString(Command):
    """
    move Cursor ToStart String
    """
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorToStringStart()
class moveCursorToEndString(Command):
    """
    move cursor to end string
    """
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorToStringEnd()
class moveCursorToRightWordEnd(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorToRightWordEnd()
class moveCursorToLeftWordStart(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorToLeftWordStart()
class moveCursorToFileStart(Command):
    def execute(self, *args: None)-> bool:
        print("moveCursorToFileStart")
        return self._editor.moveCursorToFileStart()
class moveCursorToFileEnd(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.moveCursorToFileEnd()
class moveCursorToNstring(Command):
    def execute(self, *args: int)-> bool:
        """
        :param args: only 1 is N - number of string
        :type args: int
        """
        print("moveCursorToNstring")
        return self._editor.moveCursorToNstring(args[0])
class moveScreenToUp(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.moveScreenToUp()
class moveScreenToDown(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.moveScreenToDown()
class deleteSymbolAfterCursor(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.deleteSymbolAfterCursor()
class deleteWordUnderCursor(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.deleteWordUnderCursor()
class cutCurrentString(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.cutCurrentString()      
class copyCurrentString(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.copyCurrentString()
class copyWordUnderCursor(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.copyWordUnderCursor()
class pasteAfterCursor(Command):
    def execute(self, *args: None)-> bool:
        return self._editor.pasteAfterCursor()

"""
Insert Mode
"""
class insertText(Command):
    def  execute(self, *args)-> bool:
        status = self._editor.insertText(args[0])
        if (status == False):
            return status
        status = self._editor.moveCursorRight(1)
        return status
class insertTextInStartString(Command):
    def  execute(self, *args)-> bool:
        return self._editor.insertTextInStartString()
class insertTextInEndString(Command):
    def  execute(self, *args)-> bool:
        return self._editor.insertTextInEndString()
class deleteStringToInsert(Command):
    def  execute(self, *args)-> bool:
        return self._editor.deleteStringToInsert()
class replaceSymbolUnderCursor(Command):
    def  execute(self, *args)-> bool:
        return self._editor.replaceSymbolUnderCursor(args[0])

"""
Search State
"""
class searchFromCursorToEndFile(Command):
    """
    if find text Cursor will place in start text
    """
    def execute(self, *args)-> bool:
        return self._editor.searchFromCursorToEndFile(args[0])
class searchFromCursorToStartFile(Command):
    """
    if find text Cursor will place in start text
    """
    def execute(self, *args)-> bool:
        return self._editor.searchFromCursorToStartFile(args[0])
        
class research(Command):
    """
    repeat search
    """
    def execute(self, *args)-> bool:
        print("researh")
        self._editor.research(args[0])
        return True
class researchInvers(Command):
    """
    search on the contrary 
    """
    def execute(self, *args)-> bool:
        print("researchInvers")
        self._editor.researchInvers(args[0])
        return True

"""
Command State
"""
class open(Command):
    def execute(self, *args)-> bool:
        return self._editor.open(args[0])
class writeExit(Command):
    def execute(self, *args)-> bool:
        return self._editor.writeFile()
class write(Command):
    def execute(self, *args)-> bool:
        return self._editor.writeFile()
class writeFile(Command):
    def execute(self, *args)-> bool:
        return self._editor.writeFile(args[0])
class quitAfterSave(Command):
    def execute(self, *args)-> bool:
        return self._editor.quit(False)
class quitWithoutSave(Command):
    def execute(self, *args)-> bool:
        print("quitWithoutSave")
        return self._editor.quit(True)
class writeQuit(Command):
    def execute(self, *args)-> bool:
        return self._editor.writeQuit()
class placeNstring(Command):
    def execute(self, *args)-> bool:
        return self._editor.moveCursorToNstring(args[0])
class TurnOnOffNumStrings(Command):
    def execute(self, *args)-> bool:
        return self._editor.TurnOnOffNumStrings()
class help(Command):
    def execute(self, *args)-> bool:
        return self._editor.showHelp()


