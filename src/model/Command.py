from .Data import Data

class Command():
    def __init__(self, editor: Data):
        self._editor = editor

    def execute(self):
        pass