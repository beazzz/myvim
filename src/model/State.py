from .Data import State
from .Command import rightCommand

class NormalState(State):
    """
    state for navigate and edit
    """
    def __init__(self, context):
        super().__init__(context)
        self.addCommmand("right", rightCommand(self._context))

class InsertState(State):
    pass

class VisualState(State):
    pass

class CommandState(State):
    pass

