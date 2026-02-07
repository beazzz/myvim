from model.Data import Data
import model.Command
import model.State as State
from view.View import View
import curses


def main():
    # init
    # test = Data()
    # test.AddState("Command", State.CommandState(test))
    # test.AddState("Insert", State.InsertState(test))
    # test.AddState("Search", State.SearchState(test))
    # test.AddState("Normal", State.NormalState(test))
    
    # test.ChangeState("Command")
    # #test.handleInput("esc")
    # test.handleInput("esc")
    # # test.ChangeState("Co")
    # # test.handleInput("o", "test.txt")
    # # test.handleInput("w")
    # print(test)
    # print()
    # # print("!!!", test.getPosCursor())
    canvas = curses.initscr()

    print(canvas.getkey())

if __name__ == '__main__':
    main()