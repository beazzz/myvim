from .Data import Command

class rightCommand(Command):
    def execute(self):
        print("right completed", self)
        self._editor.posCursor('x', 1)