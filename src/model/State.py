from .Data import State
import Command

class NormalState(State):
    """
    state for navigate and edit
    """
    def __init__(self, context):
        super().__init__(context)
        self.addCommmand("right", Command.rightCommand(self._context))
        self.addCommmand("left", Command.leftCommand(self._context))
        self.addCommmand("up", Command.upCommand(self._context))
        self.addCommmand("down", Command.downCommand(self._context))
        self.addCommmand("0", Command.ZeroCommand(self._context))
        self.addCommmand("$", Command.DollarCommand(self._context))

class InsertState(State):
    pass

class VisualState(State):
    pass

class CommandState(State):
    pass

