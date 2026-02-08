from controller.Controller import ClientController
import curses

def main():
    control = ClientController()
    print()
    control.handleInput("g")
    print()
    control.handleInput("g")

if __name__ == '__main__':
    main()