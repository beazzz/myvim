from controller.Controller import Controller
import curses

def main():
    canvas = curses.initscr()

    print(canvas.getkey())

if __name__ == '__main__':
    main()