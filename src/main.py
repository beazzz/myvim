from model.Data import Data
import model.Command
import model.State as State
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Command", State.CommandState(test))
    test.ChangeState("Command")

    print(test)
    print()
    test.handleInput("h")
    # print("!!!", test.getPosCursor())

if __name__ == '__main__':
    main()