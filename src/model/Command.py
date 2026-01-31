from .Data import Command

class rightCommand(Command):
    """
    move cursor right
    """
    def execute(self):
        self._editor.moveCursorRight()
        
class leftCommand(Command):
    """
    move cursor left
    """
    def execute(self):
        self._editor.moveCursorLeft()
class upCommand(Command):
    """
    move cursor up
    """
    def execute(self):
        self._editor.moveCursorUp()
class downCommand(Command):
    """
    move cursor down
    """
    def execute(self):
        self._editor.moveCursorDown()
  
