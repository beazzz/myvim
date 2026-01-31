from .Data import State
from .Command import rightCommand

class NormalState(State):
    def __init__(self, context):
        super().__init__(context)

        self.addCommmand("right", rightCommand(self._context))

class InsertState(State):
    pass

class VisualState(State):
    pass

class CommandState(State):
    pass

