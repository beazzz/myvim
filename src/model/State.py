from .Command import Command

class State():
    def __init__(self):
        self._commands = []
    
    def handleInput(self, command : Command):
        self._commands[command].execute()

    def addCommmand(self):
        pass

    def ChangeState(self):
        pass