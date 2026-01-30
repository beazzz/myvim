from .Command import Command

class State():
    def __init__(self):
        self._commands: list[Command] = []
    
    def handleInput(self, commandName):
        self._commands[commandName].execute()

    def addCommmand(self):
        pass

    def ChangeState(self):
        pass