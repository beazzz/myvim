from .Data import Command

class rightCommand(Command):
    """
    move cursor right
    """
    def execute(self):
        cursor = self._editor.getPosCursor()
        cursor['x'] += 100

        if cursor['x'] > len(self._editor.getRaw()): 
            cursor['x'] = 0
            cursor['y'] += 1

        self._editor.posCursor(cursor)
        print("right completed", self)


class leftCommand(Command):
    """
    move cursor left
    """
    def execute(self):
        cursor = self._editor.getPosCursor()
        cursor['x'] -= 1

        if cursor['x'] < 0:
            if cursor['y'] == 0:
                cursor['x'] = 0
            else:
                cursor['x'] = len(self._editor.getRaw())
                cursor['y'] -= 1

        self._editor.posCursor(cursor)
        print("left completed", self)
        
