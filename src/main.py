from controller.Controller import ClientController
import curses

def main():
    control = ClientController("test.txt")
    # canvas = curses.initscr()
    #print(int(canvas.getkey()))
    # print('\n' == canvas.getkey())
    # print(canvas.getkey())
    # print(canvas.getkey())
    # control.handleInput("\x1b")
    
    done = False
    while not done:
        # print("draw")
        control.draw()
        # print("execute")
        control.execute()

        done = control.close()
    
    # print(str(curses.KEY_UP))

if __name__ == '__main__':
    main()