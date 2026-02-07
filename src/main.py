from controller.Controller import ClientController
import curses

def main():
    control = ClientController()
    control.execute()

if __name__ == '__main__':
    main()