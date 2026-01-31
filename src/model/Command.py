from .Data import Command

class rightCommand(Command):
    """
    move cursor right
    """
    def execute(self):
        print("right completed", self)
        self._editor.posCursor('x', 1)