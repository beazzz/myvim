from controller.Controller import ClientController
import curses

def main():
    control = ClientController("test.txt")
    
    done = False
    while not done:
        control.draw()
        control.execute()

        done = control.close()

if __name__ == '__main__':
    main()
