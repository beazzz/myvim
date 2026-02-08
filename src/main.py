from controller.Controller import ClientController
import curses

def main():
    control = ClientController()
    print()
    control.handleInput("g")
    print()
    control.handleInput("g")

    print()
    control.handleInput("3")
    print()
    control.handleInput("G")
    # a = ""
    # a += "3"
    # a += "5"
    # print([int(a)])

if __name__ == '__main__':
    main()