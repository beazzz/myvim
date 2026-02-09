from controller.Controller import ClientController
import curses

def main():
    control = ClientController("test.txt")
    # canvas = curses.initscr()
    # canvas.keypad(True)
    # print(int(canvas.getkey()))
    # print('\n' == canvas.getkey())
    # print(canvas.getkey())
    # print(canvas.getkey())
    # control.handleInput("\x1b")
    
    while True:
        print("draw")
        control.draw()
        print("execute")
        control.execute()
    
    # print(str(curses.KEY_UP))

if __name__ == '__main__':
    main()