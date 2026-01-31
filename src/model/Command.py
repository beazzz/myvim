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
  
