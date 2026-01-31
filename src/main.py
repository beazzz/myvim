from model.Data import Data
from model.Command import downCommand
from model.State import NormalState
from view.View import View


def main():
    # init
    test = Data("test.txt")
    test.AddState("Normal", NormalState(test))
    test.ChangeState("Normal")

    test.handleInput("down")
    test.handleInput("down")
    test.handleInput("down")
    test.handleInput("down")
    test.handleInput("down")
    test.handleInput("down")
    print(test.getPosCursor())


if __name__ == '__main__':
    main()